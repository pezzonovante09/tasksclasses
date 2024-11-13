# class A:
#     def public(self):
#         return 'public'
    
#     def _protected(self):
#         return 'protected'
    
#     def __private(self):
#         return 'private'
    
# obj = A()
# print(obj.public())
# print(obj._protected())
# print(obj._A__private())

# class Car:
#     def __init__(self, speed):
#         self.__speed = speed

#     def get_speed(self):
#         return self.__speed
    
#     def set_speed(self, new_speed):
#         self.new_speed = new_speed
#         if self.new_speed >= 0:
#             self.__speed = self.new_speed
#             return f'Speed = {self.__speed}'
#         else:
#             return 'Speed must be higher than zero'

# obj = Car(0)
# print(obj.set_speed(50))

# class Car:
#     def __init__(self, speed):
#         self.__speed = speed

#     @property
#     def get_speed(self):
#         return self.__speed
    
#     @get_speed.setter
#     def set_speed(self, new_speed):
#         if new_speed >= 0:
#             self.__speed = new_speed
#             return f'Speed = {self.__speed}'
#         else:
#             raise Exception('Speed must be higher than zero')

# obj = Car(0)
# obj.set_speed = 50
# print(obj.set_speed)
# obj.set_speed = -20
# print(obj.set_speed)
        

# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number

#     def get_name(self):
#         return self.name
    
#     def get_p(self):
#         return self._phone_number
    
#     def get_c(self):
#         return self.__card_number
    
# obj = Person('Pork', 12345, 101012)
# print(obj.get_name())
# print(obj.get_p())
# print(obj.get_c())


# class Game:
#     def __init__(self, level, name):
#         self.__level = level
#         self.name = name

#     def play(self):
#         a ='wth'
