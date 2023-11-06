from ast import FormattedValue
import unittest
from name_function import get_formatted_name

class NamesTestCases(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Rejoan Siddiky' work?"""
        formatted_name = get_formatted_name('rejoan', 'siddiky')
        self.assertEqual(formatted_name, 'Rejoan Siddiky')
    
    def test_first_last_middle_name(self):
        """Do names like 'Rejoan Xyz Siddiky' work?"""
        formatted_name = get_formatted_name('rejoan', 'siddiky', 'xyz')
        self.assertEqual(formatted_name, 'Rejoan Xyz Siddiky')

if __name__ == '__main__':
    unittest.main()