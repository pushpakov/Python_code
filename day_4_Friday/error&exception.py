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



import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise