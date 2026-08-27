from unittest import TestCase


class TestBasic(TestCase):
    def test_basic(self):
        value = 10
        self.assertEqual(value, 10)
