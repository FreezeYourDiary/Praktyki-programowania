import unittest
from main import Add

class MyTestCase(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        self.assertEqual(Add(""),0)

    def test_single_number_returns_value(self):
        self.assertEqual(Add("1"),1)

    def test_two_numbers_returns_sum(self):
        self.assertEqual(Add("1,2"),3)

    def test_wrong_input(self):
        with self.assertRaises(ValueError):
            Add(",,5,gg");

    def test_multiple_numbers(self):
        self.assertEqual(Add("5,5,10"),20)
        self.assertEqual(Add("15,10,25"), 50)

    def test_new_line(self):
        self.assertEqual(Add("5\n10,5"),20)

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            self.assertEqual(Add("1,\n\n\n6"),1)

if __name__ == '__main__':
    unittest.main()
