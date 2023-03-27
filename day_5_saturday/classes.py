# # scope in python 
# # the four scope in python follow the LEGB rule to search for the variable
# # the example with illustration is below 

# # Global scope
# global_var = 100

# class MyClass:
#     # Class scope
#     class_var = 50

#     def __init__(self, x):
#         # Instance scope
#         self.x = x

#     def my_method(self):
#         # Local scope
#         local_var = 10
#         print("Local variable:", local_var)
#         print("Instance variable:", self.x)
#         print("Class variable:", MyClass.class_var)
#         print("Global variable:", global_var)

#     def outer_method(self):
#         # Enclosing scope
#         outer_var = 20

#         def inner_method():
#             # Local scope
#             inner_var = 30
#             print("Local variable:", inner_var)
#             print("Enclosing variable:", outer_var)
#             print("Instance variable:", self.x)
#             print("Class variable:", MyClass.class_var)
#             print("Global variable:", global_var)

#         inner_method()

# # Creating an object of MyClass
# obj = MyClass(5)

# # Calling my_method() to access local, instance, class, and global variables
# obj.my_method()

# # Calling outer_method() to access enclosing, instance, class, and global variables
# obj.outer_method()

# # a simple class without init method 
# class MyClass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'hello world'

# class_instance = MyClass()  #instance of the class is created 
# print(MyClass.f("")) # this will be similar to the  class_instance.f() but here the instance of the class is not created 
# print(class_instance.f()) 



# # creating a class with the argument passed to the initilization method of the class
# class Complex:
#      y = 10      #class variable shared by all the instance of the class
#      def __init__(self, realpart, imagpart):
#          self.r = realpart                          #instance variable unique to each instance 
#          self.i = imagpart                          #instance variable unique to each instance 
 
# x = Complex(3.0, -4.5)
# y = Complex(1,2)
# print(x.r, x.i)


# # defining a variable as the data attribute for the object 
# x.num = 1
# while(x.num<=10):
#     print(x.num)
#     x.num+=1

# print(x.num)                                        #unique to the instance x
# print(y.y)                                           #shared by all the instance 
# print(x.y)                                           #shared by all the instance 
# del x.num



# # isinstance() method and issubclass() method 

# class Animal:
#     pass

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# # Example of isinstance method
# dog = Dog()
# cat = Cat()
# animal = Animal()

# print(isinstance(dog, Dog))    # Output: True
# print(isinstance(cat, Animal)) # Output: True
# print(isinstance(animal, Cat)) # Output: False

# # Example of issubclass method
# print(issubclass(Dog, Animal)) # Output: True
# print(issubclass(Cat, Dog))    # Output: False
# print(issubclass(Animal, Cat)) # Output: False


# # multiple inheritance 

# class Parent1:
#     def method1(self):
#         print("This is method 1 from Parent 1.")

# class Parent2:
#     def method2(self):
#         print("This is method 2 from Parent 2.")

# class Child(Parent1, Parent2):     # here the class is inherating from two different class 
#     pass

# child = Child()
# child.method1() # Output: "This is method 1 from Parent 1."
# child.method2() # Output: "This is method 2 from Parent 2."



# # multi-level inheritance with example 

# class Grandparent:
#     def method1(self):
#         print("This is method 1 from Grandparent.")

# class Parent(Grandparent):
#     def method2(self):
#         print("This is method 2 from Parent.")

# class Child(Parent):
#     def method3(self):
#         print("This is method 3 from Child.")

# class Grandchild(Child):
#     def method4(self):
#         print("This is method 4 from Grandchild.")

# grandchild = Grandchild()                      # here the grandchild will have all the characterstics of child class, parent class, and grandparent
# grandchild.method1() # Output: "This is method 1 from Grandparent."
# grandchild.method2() # Output: "This is method 2 from Parent."
# grandchild.method3() # Output: "This is method 3 from Child."
# grandchild.method4() # Output: "This is method 4 from Grandchild."



# # private variable in class
# class MyClass:
#     def __init__(self):
#         self.public_variable = "This is a public variable"
#         self.__private_variable = "This is a private variable"
    
#     def update(self, y):
#         self.__private_variable = y

#     __private_variable = "This is updated private variable"
    
        
# my_object = MyClass()

# print(my_object.public_variable)   # This will print "This is a public variable"
# # print(my_object.__private_variable)  # This will raise an AttributeError


# # updating the privare variable in class as we cannot access the private variable in outside the class
# class MyClass:
#     def __init__(self):
#         self.public_variable = "This is a public variable"
#         self.__private_variable = "This is a private variable"
        
#     def update_private_variable(self, new_value):
#         self.__private_variable = new_value
    
#     def get_private_variable(self):
#         return self.__private_variable

# my_object = MyClass()

# print(my_object.get_private_variable())   # This will print "This is a private variable"
# my_object.update_private_variable("New value for private variable")
# print(my_object.get_private_variable())   # This will print "New value for private variable"


# # iterators 
# for element in [1, 2, 3]:
#     print("list",element)
# for element in (1, 2, 3):
#     print("tuple",element)
# for key in {'one':1, 'two':2}:
#     print("dict",key)
# for char in "123":
#     print("char",char)














