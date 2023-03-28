# Polymorphism simply means more than one form.
# That means the same entity (method or operator or object) can perform different operations in different scenarios.


class Polygon:
    # render a shape
    def render(self) -> None:
        print("Rendering Polygon...")

class Square(Polygon):
    # renders Square
    def render(self) -> None:
        print("Rendering Square...")

class Circle(Polygon):
    # renders circle
    def render(self) -> None:
        print("Rendering Circle...")
    
# create an object of Square
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()

try:
    # create an object of Polygon (which is abstract)
    p = Polygon()
    p.render()
except TypeError as e:
    print(f"Error: {e}")







# another example 
print("OTHER EXAMPLE  : ----------------------------------------------")

class Animal:                 #  abstract class
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof woof!"

class Cat(Animal):
    def speak(self):
        return "Meow meow!"

dog = Dog("Rufus")
cat = Cat("Whiskers")

print(dog.speak())  #  "Woof woof!"
print(cat.speak())  #  "Meow meow!"
