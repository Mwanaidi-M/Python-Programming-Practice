class MyClass:
    """ Sample class to see how instance/class/static methods can be used """
    def method(self):
        return f"Instance method called here: {self}\n"

    @classmethod
    def class_method(cls):
        return f"Class method has been called here: {cls}\n"

    @staticmethod
    def static_method():
        return f"Called a static method here.\n"


obj1 = MyClass()
print(obj1.class_method())
