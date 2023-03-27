# make a class that will reverse a string using the __next__, __iter__ method

class EmptyStringError(Exception):
    def __str__(self) -> str:
        return "Input string cannot be empty"

class ReverseString:
    def __init__(self, s: str) -> None:
        if not s:
            raise EmptyStringError()
        self.s = s
        self.index = len(s)

    def __iter__(self) -> "ReverseString":
        # print(self.s)
        return self

    def __next__(self) -> str:
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        # print(self.s[self.index])
        return self.s[self.index] 

while True:
    try:
        s = input("Enter a string to reverse: ")
        reversed_string = "".join((list(ReverseString(s))))
        print("Reversed string:", reversed_string, end="")
        break
    except EmptyStringError as e:
        print("Error:", e)
