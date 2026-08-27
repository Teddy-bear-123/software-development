from enum import Enum

from range import Range


class StorageBackend:
    """Storage backend to be plugged under the cache."""

    def pwrite(self, data: bytearray, offset) -> int:
        return -1

    def pread(self, offset, size) -> bytearray:
        return bytearray()


class CacheEntryState(Enum):
    """State (dirty or not) of a cache entry."""

    NEW = 1
    CLEAN = 2
    DIRTY = 3


class CacheEntry:
    """A data segment mapped on a specific range, with a clean/dirty/new state."""

    def __init__(self, offset, size):
        self.range = Range(offset, size)
        self.state = CacheEntryState.NEW
        self.data = bytearray(size)


class Cache:
    """A cache which can store data and flush it to a storage backend.

    A read automatically fetches data not already present in the cache.
    """

    def __init__(self, backend: StorageBackend):
        self.backend = backend
        self.entries = []

    def pwrite(self, data, offset):
        op_range = Range(offset, len(data))
        self._create_entries(op_range.offset, op_range.size)

        for entry in self.entries:
            if Range.overlap(entry.range, op_range):
                intersect = Range.intersect(op_range, entry.range)
                in_data_range = intersect.shift(-offset)
                out_data_range = intersect.shift(-entry.range.offset)
                entry.data[out_data_range.offset:out_data_range.end()] = data[
                    in_data_range.offset:in_data_range.end()
                ]
                entry.state = CacheEntryState.DIRTY

    def pread(self, offset, size) -> bytearray:
        op_range = Range(offset, size)
        self._create_entries(op_range.offset, op_range.size)
        self._apply_read_on_new_entries()

        out_data = bytearray(size)
        for entry in self.entries:
            if Range.overlap(entry.range, op_range):
                intersect = Range.intersect(op_range, entry.range)
                out_data_range = intersect.shift(-offset)
                in_data_range = intersect.shift(-entry.range.offset)
                out_data[out_data_range.offset:out_data_range.end()] = entry.data[
                    in_data_range.offset:in_data_range.end()
                ]
        return out_data

    def flush(self, range: Range = Range(0, 0)):
        for entry in self.entries:
            if entry.state == CacheEntryState.DIRTY and (
                range.size == 0 or Range.overlap(range, entry.range)
            ):
                res = self.backend.pwrite(entry.data, entry.range.offset)
                if res != entry.range.size:
                    raise Exception("Fail to fully write data into storage backend")
                entry.state = CacheEntryState.CLEAN

    def _get_sort_key(entry: CacheEntry):
        return entry.range.offset

    def _create_entries(self, offset, size):
        cur_range = Range(offset, size)

        for i in range(len(self.entries)):
            entry = self.entries[i]
            if Range.overlap(cur_range, entry.range):
                left, right = Range.exclude(cur_range, entry.range)
                if left.size > 0:
                    self.entries.append(CacheEntry(left.offset, left.size))
                cur_range = right
            if cur_range.size == 0:
                break

        if cur_range.size != 0:
            self.entries.append(CacheEntry(cur_range.offset, cur_range.size))

        self.entries.sort(key=Cache._get_sort_key)

    def _apply_read_on_new_entries(self):
        for entry in self.entries:
            if entry.state == CacheEntryState.NEW:
                data = self.backend.pread(entry.range.offset, entry.range.size)
                if len(data) != entry.range.size:
                    raise Exception("Not enough data to read")
                entry.data = data
                entry.state = CacheEntryState.CLEAN
