import unittest
from city_functions import show_locations


class CheckLocationInput(unittest.TestCase):
    """ Test class for tests on the input """

    def test_city_country(self):
        """ Funtion to verify that calling the function with values such
        as 'santiago' and 'chile' results in the correct string.
        """
        new_format = show_locations("santiago", "chile")
        self.assertEqual(new_format, "Santiago, Chile")

    def test_city_country_population(self):
        """ Funtion to verify that calling the function with 'santiago', 'chile', and
        'population=5000000' results in the correct string.
        """
        new_format = show_locations("santiago", "chile", 5_000_000)
        self.assertEqual(new_format, "Santiago, Chile - population 5000000")


if __name__ == '__main__':
    unittest.main()
