class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize the rectangle with length and width
        self.length = length
        self.width = width

    def __iter__(self):
        # Create an iterator for the Rectangle
        yield {"length": self.length}
        yield {"width": self.width}

# Example Usage
rect = Rectangle(10, 5)

# Iterating over the Rectangle instance
for item in rect:
    print(item)
