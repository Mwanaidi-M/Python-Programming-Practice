class Employee:
    """ Class that takes employee's first & last name as well as their salary """

    def __init__(self, first_name, last_name, salary):
        """ method that takes in a first name, a last name, and an annual salary """
        self.fname = first_name
        self.lname = last_name
        self.salary = salary

    def give_raise(self, e_salary=5_000):
        """ method that adds $5,000 to the annual salary by default but also accepts a
        different raise amount.
        """
        new_salary = self.salary + e_salary

        print(f"Previous Salary: ${self.salary}")
        print(f"New Salary: ${new_salary}\n")

        return new_salary
