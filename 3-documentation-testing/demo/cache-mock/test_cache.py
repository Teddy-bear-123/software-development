from unittest import TestCase, mock

from cache import Cache, StorageBackend


class ManualMockBackend(StorageBackend):
    def pread(self, offset, size) -> bytearray:
        return bytearray(b"Hello")

    def pwrite(self, data: bytearray, offset) -> int:
        return 5


class ManualTestCache(TestCase):
    def test_init(self):
        backend = ManualMockBackend()
        _cache = Cache(backend)

    def test_pread(self):
        backend = ManualMockBackend()
        cache = Cache(backend)

        result = cache.pread(offset=0, size=5)
        self.assertEqual(result, bytearray(b"Hello"))

    def test_pwrite(self):
        backend = ManualMockBackend()
        cache = Cache(backend)

        cache.pwrite(bytearray(b"World"), offset=0)
        result = cache.pread(offset=0, size=5)
        self.assertEqual(result, bytearray(b"World"))


class TestCache(TestCase):
    def test_init(self):
        backend = StorageBackend()
        _cache = Cache(backend)

    def test_pread_one(self):
        backend = StorageBackend()
        backend.pread = mock.MagicMock(return_value=bytearray(b"Hello"))
        cache = Cache(backend)

        result = cache.pread(offset=0, size=5)
        self.assertEqual(result, bytearray(b"Hello"))
        backend.pread.assert_called_once_with(0, 5)

    def test_pread_second_call_is_cached(self):
        backend = StorageBackend()
        backend.pread = mock.MagicMock(return_value=bytearray(b"Hello"))
        cache = Cache(backend)

        cache.pread(offset=0, size=5)
        cache.pread(offset=0, size=5)
        backend.pread.assert_called_once_with(0, 5)

    def test_pwrite_then_flush(self):
        backend = StorageBackend()
        backend.pwrite = mock.MagicMock(return_value=5)
        cache = Cache(backend)

        cache.pwrite(bytearray(b"Hello"), offset=0)
        backend.pwrite.assert_not_called()

        cache.flush()
        backend.pwrite.assert_called_once()
