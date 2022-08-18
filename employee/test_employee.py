import unittest
from employee_all import Employee


class EmployeeRaiseTest(unittest.TestCase):
    """ Test class for the Employee class"""

    def setUp(self):
        """ Creating a default Emploee instance to avoid creating one for each test. """
        self.employee = Employee("Amaya", "Johanness", 10_000)

    def test_give_default_raise(self):
        """ Method to check if a raise will be given with the default value. """

        print("With regards to a default value:")
        new_employee_salary = self.employee.give_raise()
        self.assertEqual(new_employee_salary, 15_000)

    def test_give_custom_raise(self):
        """ Method to check if a raise will be given if we provide a custom value of 15_000. """

        print("With regards to a custom value:")
        new_employee_salary = self.employee.give_raise(15_000)
        self.assertEqual(new_employee_salary, 25_000)


if __name__ == '__main__':
    unittest.main()
