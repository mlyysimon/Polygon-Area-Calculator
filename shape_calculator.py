class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2*(self.width + self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ''
      for i in range(self.height):
        picture += '*' * self.width + '\n'
      return picture

  def get_amount_inside(self, shape):
    if shape.width > self.width or shape.height > self.height:
      return 0
    else:
      return self.get_area() // shape.get_area()

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):

  def __init__(self, side):
    Rectangle.width = side
    Rectangle.height = side

  def set_side(self, side):
    Rectangle.width = side
    Rectangle.height = side

  def set_width(self, side):
    Rectangle.width = side

  def set_height(self, side):
    Rectangle.height = side

  def __str__(self):
    return f'Square(side={Rectangle.width})'