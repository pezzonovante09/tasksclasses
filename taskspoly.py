# class Device:
#     def __init__(self, brand, model, pixel) -> None:
#         self.brand = brand
#         self.model = model
#         self.pixel = pixel
        
#     def brand(self) -> None:
#         return f'Брэнд телефона - {self.brand}'
    
#     def model(self) -> None:
#         return f'Модель телефона - {self.model}'
    
#     def pixel(self) -> None:
#         return f'Пиксели - {self.pixel}'
    
# class Iphone16(Device):
#     def __init__(self, brand, model, pixel) -> None:
#         self.brand = brand
#         self.model = model
#         self.pixel = pixel
#     def brand1(self) -> None:
#         return super().brand()
#     def model1(self) -> None:
#         return super().model()
#     def pixel1(self) -> None:
#         return super().pixel()
    
# obj = Iphone16('Iphone', 16, 144)
# print(obj.brand1())
# print(obj.model1())
# print(obj.pixel1())


# class Car:
#     def __init__(self, max_speed, weight) -> None:
#         self.max_speed = max_speed
#         self.weight = weight

#     def time(self) -> None:
#         return f'Время прохождения - {self.max_speed/100 * 3.14}'
    
# class Lexus(Car):
#     def __init__(self, max_speed, weight) -> None:
#         self.max_speed = max_speed
#         self.weight = weight
#     def time(self) -> None:
#         return super().time()
    
# class Porsche(Car):
#     def __init__(self, max_speed, weight) -> None:
#         self.max_speed = max_speed
#         self.weight = weight
#     def time(self) -> None:
#         return super().time()
    
# obj = Lexus(1500000, 1000)
# obj1 = Porsche(260000, 1500)
# print(obj.time())
# print(obj1.time())

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def eat(self, food) -> None:
#         self.food = food
#         return f'Я кушаю {self.food}'
# class Reader(Person):
#     def __init__(self, number, phone) -> None:
#         super().__init__('Ivan', 18)
#         self.number = number
#         self.phone = phone
    
#     def take_book(self, book_name) -> None:
#         self.book_name = book_name
#         return f'{self.name} взял {self.book_name}'
    
#     def return_book(self, book_name) -> None:
#         self.book_name = book_name
#         return f'{self.name} вернул {self.book_name}'
    
#     def eat(self, food) ->None:
#         print(f'Я {self.name} и я не кушаю {food}, а предпочитаю книги')

# obj = Reader(55, 99683189319)
# print(obj.take_book('Граф'))
# print(obj.return_book('Граф'))
# print(obj.eat('Ананас'))

# class Student:
#     def __init__(self, name, group, average_mark) ->None:
#         self.name = name
#         self.group = group
#         self.average_mark = average_mark
    
#     def get_scholarship(self) -> None:
#         if self.average_mark == 5:
#             return 2000
#         else:
#             return 1500

# class Aspirant(Student):
#     def __init__(self, name, group, average_mark) -> None:
#         super().__init__(name, group, average_mark)
#     def get_scholarship(self):
#         money = 0
#         if self.average_mark == 5:
#             return 3000
#         else:
#             return 2500
        
# obj = Aspirant('Graf', '12', 5)
# print(obj.get_scholarship())

class Money:
    def __init__(self, country, symbol) -> None:
        self.country = country
        self.symbol = symbol

class Euro(Money):
    def __init__(self, country, symbol):
        super().__init__(country, symbol)
    def exchange(self, money) -> None:
        self.money = money
        if self.country == 'USA' and self.symbol == '$':
            return f'{money / 80}$ are equal to {money}soms'
        elif self.country == 'Europe' or self.symbol == '€':
            return f'{money / 100}$ are equal to {money}soms'
        
obj = Euro('USA', '$')
print(obj.exchange(1000))