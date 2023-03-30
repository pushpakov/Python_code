"""
class method is a method that is bound to the class and not the instance of the class. It is used to create methods that can access and modify the class-level variables, and it takes the class as the first argument (usually named cls). A class method is defined using the @classmethod decorator
"""

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Example usage
a = MyClass()
b = MyClass()
print(MyClass.get_count())  # Output: 2


