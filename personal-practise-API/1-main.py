class Persona:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        
    @property
    def getname(self):
        return self.name
    
    @getName.setter #El conjunto de getter y setter se conoce como encapsulamiento (Investigar)
    def setName(self, value: str):
        if not isinstance (str, value):
            print("Que haces mogo")
        if len(value) >= 2000:
            print("No seas boludo")
        self.name = value