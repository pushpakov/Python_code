# syntax error is the error that occurs when python is not able to interpret the code due to error in the syntax
# example of syntax error 

# x = int(input("Enter the integer : "))
# if x>10:       # here if we will remove the : then it will throw syntax error as the syntax will become invalid 
#     print("hello ")
# else:
#     print("sorry") 


# # zero division error
# print(1/0)         # this will throw zerodivision error 

# # name error 
# print(pushpak) # this will throw NameError : name 'pushpak' is not defined

# # type error 
# print("2"+22)  # this will throw TypeError can only concatenate str (not "int") to str


# # handling exceptions in code using try and except 
# while True:
#     try:
#         x = int(input("Enter the integer value : "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")


# # to raise the error manually we can use raise keyword with the error message along with the type of error we want to provide
# x = -1
# if x < 0:
#     raise ValueError("x should be positive number")


# # # Python code block that uses a try-except block to handle possible errors that may occur during the execution of the code

# import sys

# try:
#     # x = 1/0
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise


# # else clause in try except exception handling 
# try:
#     # Code that may raise an exception
#     x = int(input("Enter a number: "))
#     y = int(input("Enter another number: "))
#     result = x / y
# except ZeroDivisionError:
#     # Code to handle a specific exception
#     print("Cannot divide by zero.")
# except ValueError:
#     # Code to handle a specific exception
#     print("Invalid input. Please enter a number.")
# else:
#     # Code to be executed if no exception is raised
#     print("Result:", result)


# # exception using the argument 
# try:
#      raise Exception('spam', 'eggs')
# except Exception as inst:
#      print(type(inst))    # the exception instance
#      print(inst.args)     # arguments stored in .args
#      print(inst)          # __str__ allows args to be printed directly,
#                           # but may be overridden in exception subclasses
#      x, y = inst.args     # unpack args
#      print('x =', x)
#      print('y =', y) 

# print(Exception.args)    # this will print attribute args of base exception object

# #  a simple way is to re-raise the unhandled exception to show the exception in the code using raise keyword
# try:
#     raise NameError("hello")
# except NameError:
#     print("an exception has occured")
#     raise


# # # user defined exception with example 

# class Error(Exception):
#     pass

# class InputError(Error):
#     def __init__(self, expression, message):
#         self.expression = expression
#         self.message = message

# class TransitionError(Error):
#     def __init__(self, previous, next, message):
#         self.previous = previous
#         self.next = next
#         self.message = message



# def divide(x, y):
#     if y == 0:
#         raise InputError('division by zero', 'second argument cannot be zero')
#     else:
#         return x / y
# try:
#     result = divide(10, 0)
# except InputError as e:
#     print('InputError:', e.message)


# pre-defined clean up actions 
# """The first block of code opens a file in read mode using the open() function, then reads each line of the file using a for loop, and prints it to the console. This method has the disadvantage of leaving the file open even after the program has finished executing, which can cause issues if the file is being accessed by another program or user.

# The second block of code also opens the file in read mode, but instead of using a for loop to iterate over each line, it uses a with statement and the open() function to create a context in which the file is automatically closed once the block of code is finished executing. This method is considered safer and more efficient, as it ensures that the file is properly closed and resources are released when they are no longer needed.
# """
# for line in open("python/README.md"):
#     print(line, end="")


# with open("python/README.md") as f:
#     for line in f:
#         print(line, end="")

