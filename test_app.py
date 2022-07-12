import unittest
from unittest.mock import Mock

from mycsv import csvparser


class TestMethods(unittest.TestCase):
    def test_read_row(self):
        file = Mock()
        file.configure_mock(**{'readline.return_value': "\"First\",\"Second\""})


if __name__ == "__main__":
    unittest.main()
