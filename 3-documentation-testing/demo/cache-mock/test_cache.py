from unittest import TestCase, mock

from cache import Cache, StorageBackend


class ManualMockBackend(StorageBackend):
    # TODO: build a manual mock: hardcode what pread/pwrite return, no real storage.
    # A bytearray for pread (e.g. b"Hello"); a fixed size for pwrite (5, for "Hello").
    #
    # def pwrite(self, data: bytearray, offset) -> int:
    # def pread(self, offset, size) -> bytearray:
    pass


class ManualTestCache(TestCase):
    def test_init(self):
        backend = ManualMockBackend()
        cache = Cache(backend)

    def test_pread(self):
        # 1 - build a manually mocked backend
        # 2 - build a cache on top of it
        # 3 - call pread
        # 4 - check you get back the same data the mock was set up to return
        raise NotImplementedError("TODO: test pread() with the manual mock")

    def test_pwrite(self):
        # 1 - build a manually mocked backend
        # 2 - build a cache on top of it
        # 3 - call pwrite with a different pattern
        # 4 - check the cache entry was updated (and marked dirty)
        raise NotImplementedError("TODO: test pwrite() with the manual mock")


class TestCache(TestCase):
    def test_init(self):
        backend = StorageBackend()
        cache = Cache(backend)

    def test_pread_one(self):
        # 1 - build a StorageBackend and mock its pread with unittest.mock
        #     (return value: b"Hello")
        # 2 - build a cache on top of it
        # 3 - call pread(offset=0, size=5)
        # 4 - check the result matches b"Hello"
        # 5 - check the mock was called once (assert_called_once_with)
        raise NotImplementedError("TODO: test pread() with unittest.mock")

    def test_pread_second_call_is_cached(self):
        # 1 - same setup as test_pread_one
        # 2 - call pread(0, 5) twice
        # 3 - the backend mock should still have been called only once —
        #     the second read is served from the cache
        raise NotImplementedError("TODO: test that a repeated read hits the cache")

    def test_pwrite_then_flush(self):
        # 1 - build a StorageBackend and mock its pwrite (return value: 5)
        # 2 - build a cache, call pwrite(b"Hello", offset=0)
        # 3 - check the backend mock has NOT been called yet
        # 4 - call cache.flush()
        # 5 - check the backend mock has now been called once
        raise NotImplementedError("TODO: test that pwrite defers to flush()")
