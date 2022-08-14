""" Some classes that can be imported and used. """


class Restaurant:
    """ An example of class creation"""

    def __init__(self, restaurant_name, cuisine, number_served=0):
        """ Initialize the name and age attribute """
        self.restaurant = restaurant_name
        self.cuisine = cuisine
        self.number_served = number_served

    def describe_restrnt(self):
        """ Show more info about the restaurant"""
        print(f"{self.restaurant} is one of the popular restaurants.")
        print(f"{self.restaurant} specializes in {self.cuisine} cuisine.\n")

    def open_restrnt(self):
        """ Restaurant is open """
        print(f"{self.restaurant} is open. Welcome!")

    def set_number_served(self, num):
        """ Change the number of people served """
        self.number_served += num


# creating an object / instance of a class
r_cj = Restaurant("CJ's", "Mixed")


# print(f"There is a place called {r_cj.restaurant}.\n")
#
# r_cj.describe_restrnt()
# r_cj.open_restrnt()
#
# print(f"{r_cj.restaurant} has served {r_cj.number_served} customers today")
# r_cj.set_number_served(23)
# print(f"{r_cj.restaurant} has served {r_cj.number_served} customers today.")


class IceCreamStand(Restaurant):
    """An IceCream class that inherits from Restaurant"""

    def __init__(self, restaurant_name, cuisine, number_served=0):
        """Inheriting the attributes from the parent class"""
        super().__init__(restaurant_name, cuisine, number_served=0)

        #         added a special attribute
        self.flavors = ['blueberry', 'mango', 'coconut']

    def show_flavors(self):
        print(f"There are the following flavors: {', '.join(self.flavors)}")


ice1 = IceCreamStand('Planet Yogurt', 'Sweet')

# ice1.describe_restrnt()
# ice1.show_flavors()
#


class UserP:
    """Creating a User class"""

    def __init__(self, fname, lname, age, gender, email, login_attempts=0):
        """Initialize user attributes"""
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.email = email
        self.favcolor = 'black'
        self.login_attempts = login_attempts

    def show_profile(self):
        """ Show user profile """
        print(f"User Name: {self.fname} {self.lname}")
        print(f"User Gender: {self.gender}")
        print(f"Email Address: {self.email}\n")
        print(f"Login Attempts: {self.login_attempts}\n")

    def greet_user(self):
        """Say hi to user"""
        print(f"Hello {self.fname}!\n")

    def user_color(self):
        """Show user's favorite color"""
        print(f"{self.fname}'s favorite color today is {self.favcolor}")

    def update_color(self, new_color):
        """ Update the user's favorite color """
        if new_color == self.favcolor:
            print(f"Sorry you cannot rollback the color change.")
        else:
            self.favcolor = new_color

    def increment_login_attempts(self):
        """ Increase login attempts by 1 """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset value of login attempts to 0"""
        self.login_attempts = 0


person1 = UserP('Jane', 'Doe', 26, 'f', 'jdoe34@sed.com')
person2 = UserP('Andy', 'Pistro', 34, 'm', 'pistroandy@yahoo.com')

# person1.increment_login_attempts()
# person1.increment_login_attempts()
# person1.increment_login_attempts()
# person1.increment_login_attempts()
# person1.increment_login_attempts()
# person1.increment_login_attempts()
# person1.increment_login_attempts()

# person1.show_profile()

# person1.reset_login_attempts()

# person2.show_profile()
#
#
# person2.user_color()
# person2.update_color('black')
# person2.user_color()
