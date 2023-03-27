# scope in python 
# the four scope in python follow the LEGB rule to search for the variable
# the example with illustration is below 

# Global scope
global_var = 100

class MyClass:
    # Class scope
    class_var = 50

    def __init__(self, x):
        # Instance scope
        self.x = x

    def my_method(self):
        # Local scope
        local_var = 10
        print("Local variable:", local_var)
        print("Instance variable:", self.x)
        print("Class variable:", MyClass.class_var)
        print("Global variable:", global_var)

    def outer_method(self):
        # Enclosing scope
        outer_var = 20

        def inner_method():
            # Local scope
            inner_var = 30
            print("Local variable:", inner_var)
            print("Enclosing variable:", outer_var)
            print("Instance variable:", self.x)
            print("Class variable:", MyClass.class_var)
            print("Global variable:", global_var)

        inner_method()

# Creating an object of MyClass
obj = MyClass(5)

# Calling my_method() to access local, instance, class, and global variables
obj.my_method()

# Calling outer_method() to access enclosing, instance, class, and global variables
obj.outer_method()


