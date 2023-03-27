# Define custom exception for empty strings
class EmptyStringError(Exception):
    def __str__(self) -> str:
        return "Input string cannot be empty"

# Define a generator function for reversing strings
def reverse_string(s: str):
    if not s:
        # Raise EmptyStringError if input string is empty
        raise EmptyStringError()
    index = len(s)
    while index > 0:
        index -= 1 
        yield s[index] 
       

# Keep prompting the user for input until a non-empty string is entered
while True:
    try:
        s = input("Enter a string to reverse: ")
        # Create a generator for reversing the input string
        reversed_string = "".join(reverse_string(s))
        print("Reversed string:", reversed_string)
        break
    except EmptyStringError as e:
        print(e)
