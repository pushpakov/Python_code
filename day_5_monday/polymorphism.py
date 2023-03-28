# Polymorphism simply means more than one form.
# That means the same entity (method or operator or object) can perform different operations in different scenarios.


class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")

class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")

class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")
    
# here same method is called by different object and is giving different output  

# create an object of Square
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()

# create an object of Polygon
p1 = Polygon()
p1.render() 