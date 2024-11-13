"""
Абстракция
"""

"""
Абстракция - принцип ООП, в котором создается абсатрактный класс (класс - пустышка), в котором
задаются названия аттрибутов и методов, для того чтобы мы могли их переопределить в дочерних классах
У нас есть название, но нет логики
"""

from abc import ABC, abstractmethod

class AbsctractAnimal(ABC):

    @abstractmethod
    def speak(self):
        print('voice')

# obj_ = AbstractAnimal()
"""
Создавать объект от абстрактного класса нельзя
"""
class Dog(AbsctractAnimal):
    def speak(self):
        print('Bark')
    ...

obj1 = Dog()
"""
Абстракция нужна для правильности полиморфизма
@abstractmethod - декоратор, который требует переопределения метода в дочернем классе
"""
from math import pi
class AbstractShape(ABC):
    def __init__(self, name) -> None:
        self.name = name
        
    @abstractmethod
    def area(self):
        ...

class Square(AbstractShape):
    def __init__(self, length) -> None:
        super().__init__('Квадарт')
        self.length = length
    
    def area(self):
        return self.length ** 2
    
    def fact(self):
        return f'Я фигура: {self.name}'
    
class Circle(AbstractShape):
    def __init__(self, radius) -> None:
        super().__init__('Окружность')
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)
    
obj = Circle(5)
print(obj.area())