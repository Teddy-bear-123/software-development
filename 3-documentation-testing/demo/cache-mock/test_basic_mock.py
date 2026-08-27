from unittest import TestCase, mock


class ToBeMocked:
    def __init__(self):
        self.state = 0

    def complex(self, value):
        self.state += value * 8
        return self.state


class TestBasic(TestCase):
    def test_complex(self):
        obj = ToBeMocked()

        # TODO: mock obj.complex so it returns 16 without running the real body
        # ...

        res = obj.complex(10)
        self.assertEqual(res, 16)

        # TODO: check that the mock was called once, with argument 10
        # ...
