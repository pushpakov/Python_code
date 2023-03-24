# class to create user defined exception to handle exception handling and take two string from user and merge them as result to return 

class EmptyStringException(Exception):   # this is a class to create user defined exception which extends the Exception class
    pass

def merge_strings(s1, s2):
    if not s1 or not s2:
        raise EmptyStringException("One or both strings are empty") # function is calling the instance of user defined class if condition is fulfilled
    return s1 + s2

try:
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    result = merge_strings(s1, s2)
    print("Merged string:", result)
except EmptyStringException as e:
    print("Error:", str(e))
finally:
    print("Execution complete.")