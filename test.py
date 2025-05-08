"""Password Testing File"""

import unittest
from check_pwd import check_pwd

class TestPasswordFunc(unittest.TestCase):
    """Test suite for the password checking function"""

    def test1(self):
        """Test to check if an empty password is valid"""

        self.assertFalse(check_pwd(""))


if __name__ == '__main__':
    unittest.main()
