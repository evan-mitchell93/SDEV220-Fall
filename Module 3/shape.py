class Shape:
    name = "Some Shape"
    def __init__(self,color = "black"):
        self.color = color
    def __str__(self):
        return f"{self.name} as : {type(self).__name__}"
print("*" * 3, "Shape", "*" * 3)    
myShape = Shape("purple")
print(myShape.color)

class Square( Shape ):
    #shared among every instance
    name = "Square"

    def __init__(self,_x):
        super().__init__()
        self._x = _x

    def __str__(self):
        return f"{self.name} + as: {type(self).__name__}"
    
    def area(self):
        return self._x * self._x
    
mySquare = Square(5)
print("*" * 3, "Square", "*" * 3)
print(mySquare)
print(mySquare.area())
print(mySquare.color)

class Cube (Square):
    name = "Cube"
    def __init__(self, _x):
        super().__init__(_x)

    def __str__(self):
        #For demonstration purposes
        return super().__str__()
    
    def area(self):
        return 6 * self._x ** 2
    
print("*" * 3, "Cube", "*" * 3)
myCube = Cube(5)
print(myCube)
print(myCube.color)
print(myCube.name)
print(myCube.area())