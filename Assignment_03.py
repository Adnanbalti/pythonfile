class Rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width
        
    def Perimeter(self):
        return 2*(self.length + self.width)
    
    def Area(self):
        return self.length*self.width   
    
    def display(self):
        print("The length of rectangle is: ", self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.Perimeter())
        print("The area of rectangle is: ", self.Area())

myRectangle = Rectangle(4 , 7)
myRectangle.display()

