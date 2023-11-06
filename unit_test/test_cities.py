import unittest
from city_function import location

class LocationTestCase(unittest.TestCase):
    """Test for 'city_function.py'"""

    def test_city_country_name(self):
        """Do input like 'Tokyo, Japan' work?"""
        info = location("tokyo", "japan")
        self.assertEqual(info, "Tokyo, Japan")
    
    def test_city_country_population(self):
        """Do input like 'Tokyo, Japan - 160000000' wokr?"""
        info = location('tokyo', 'japan', 'population=160000000')
        self.assertEqual(info, "Tokyo, Japan - Population=160000000")

if __name__ == '__main__':
    unittest.main()