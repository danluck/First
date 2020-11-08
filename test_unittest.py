import inc_dec    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)
        self.assertEqual(inc_dec.increment(65535), 65536)
        self.assertEqual(inc_dec.increment(4294967295), 4294967296)
        self.assertEqual(inc_dec.increment(0xFFFFFFFFFFFFFFFE), 0xFFFFFFFFFFFFFFFF)
        self.assertEqual(inc_dec.increment(0xFFFFFFFFFFFFFFFF), 18446744073709551616)

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 2)
        self.assertEqual(inc_dec.decrement(-3), -4)

if __name__ == '__main__':
    unittest.main()