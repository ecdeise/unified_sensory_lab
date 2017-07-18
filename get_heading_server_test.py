import unittest
from get_heading_server import get_heading

class data_sample:
    def __init__(self):
        self.y = 10
        self.x = 20


class TestHeading(unittest.TestCase):

    def test_get_heading(self):
        ds = data_sample()
        res = get_heading(ds)
        self.assertEqual(res, 40.88899605534857)


if __name__ == '__main__':
    unittest.main()
