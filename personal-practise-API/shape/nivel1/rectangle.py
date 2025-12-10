class Rectangle:
    def __init__(self, height, width):
        self.width = width  #Al no hacer un radius protegido se genera un bucle infinito en el setter
        self.height = height

    @property
    def height(self):
        return self.height
        
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Ingresá un numero positivo gil")
        self.height = value
    
    @property
    def width(self):
        return self.width
        
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Ingresá un numero positivo gil")
        self.width = value
        
    def area(self):
        return (pi * self.radius ** 2)
    
    def perimeter(self):
        return (2 * pi * self.radius)
    
    def __str__(self):
        return f"{self.__class__.__name__}(radius={self._radius})"#Asigna el nombre de la clase dinamicamente
        
from math import pi

circle = Circle(-5.0)
print(circle.area())      # 78.539...
print(circle.perimeter()) # 31.415...
print(circle)             # Circle(radius=5.0)
