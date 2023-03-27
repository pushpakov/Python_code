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










