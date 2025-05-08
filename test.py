"""Password Testing File"""

import unittest
from check_pwd import check_pwd

class TestPasswordFunc(unittest.TestCase):
    """Test suite for the password checking function"""

    def test1(self):
        """Test to check if an empty password is valid"""
        self.assertFalse(check_pwd(""))

    def test2(self):
        """Test to check if passwords of length 8 pass"""
        self.assertTrue(check_pwd("12345678"))


if __name__ == '__main__':
    unittest.main()
