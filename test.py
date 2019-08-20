import unittest
import Open


class MyTestCase(unittest.TestCase):
    def setUp(self):
        Open.setUp()


if __name__ == '__main__':
    unittest.main(verbosity=2)