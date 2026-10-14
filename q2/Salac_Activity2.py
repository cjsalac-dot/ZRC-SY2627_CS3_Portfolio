class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return f"{self.__width:.1f}cm"

    @property
    def height(self):
        return f"{self.__height:.0f}cm"

    @width.setter
    def width(self, new_width):
        if self.__width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if self.__height > 0:
            self.__height = new_height
        else:
            print("Height must be greater than0 0")

    @width.deleter
    def width(self):
        del self.__width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self.__height
        print("Height has been deleted")


rectangle = Rectangle(3, 4)

print("Width:", rectangle.width)
print("Height:", rectangle.height)

rectangle.width = 2
rectangle.height = 9

del rectangle.width
#del rectangle.height

#print("Updated Width:", rectangle.width)
print("Updated Height:", rectangle.height)