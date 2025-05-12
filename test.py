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
        self.assertTrue(check_pwd("P@ssw0rd"))

    def test3(self):
        """Test to check if passwords of length 20 pass"""
        self.assertTrue(check_pwd("P@ssw0rdP@ssw0rd1234"))

    def test4(self):
        """Test to check if passwords of length 21 fail"""
        self.assertFalse(check_pwd("P@ssw0rdP@ssw0rd12345"))

    def test5(self):
        """Test to check if passwords with no lowercase letters are rejected"""
        self.assertFalse(check_pwd("P@SSW0RD"))

    def test6(self):
        """Test to check if passwords with a lowercase letter is accepted"""
        self.assertTrue(check_pwd("p@SSW0RD"))

    def test7(self):
        """Test to check if passwords with only lowercase letters are rejected"""
        self.assertFalse(check_pwd("p@ssw0rd"))
        
if __name__ == '__main__':
    unittest.main()
