import unittest

def c2f(c):
    return c * 1.8 + 32

class UTExampleTestcase(unittest.TestCase):

    def test_c2f(self):
        c1 = 0
        c2 = 100
        c3 = -30
        c4 = 1.5
        c5 = -1.5

        f1 = c2f(c1)
        f2 = c2f(c2)
        f3 = c2f(c3)
        f4 = c2f(c4)
        f5 = c2f(c5)

        self.assertEqual(f1,32)
        self.assertEqual(f2, 212)
        self.assertEqual(f3, -22)
        self.assertEqual(f4, 34.7)
        self.assertEqual(f5, 29.3)

if __name__ == '__main__':
    unittest.main()