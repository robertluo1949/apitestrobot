import unittest


class payTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Case1(self):
        self.assertEqual(2, 2, "testError")
    def test_Case2(self):
        self.assertEqual(2, 3, "testError")

    def test_Case3(self):
        unittest.skip("out of service")



