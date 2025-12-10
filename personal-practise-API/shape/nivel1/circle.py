class Circle:
    def __init__(self, radius):
        self._radius = radius #Al no hacer un radius protegido se genera un bucle infinito en el setter
    
    @property
    def _radius(self):
        return self._radius
        
    @_radius.setter
    def _radius(self, value):
        if value < 0:
            raise ValueError("Ingresá un numero positivo gil")
        self._radius = value
        
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
