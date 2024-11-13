from abc import ABC, abstractmethod

# class Transport(ABC):
#     @abstractmethod
#     def start(self):
#         return 'Start!'
    
#     @abstractmethod
#     def stop(self):
#         return 'Stop!'
    
# class Car(Transport):
#     def __init__(self, engine):
#         self.engine = engine

#     def start(self):
#         return f'{self.engine} has started'
    
#     def stop(self):
#         return f'{self.engine} has stopped'

# class Bicycle(Transport):
#     def __init__(self, cep):
#         self.cep = cep
    
#     def start(self):
#         return f'{self.cep} have cep'
    
#     def stop(self):
#         return f'{self.cep} doesnt have cep'
    
# obj = Car('V1')
# obj2 = Bicycle('Galaxy')

# print(obj.start())
# print(obj2.stop())


# class ElectronicDevice(ABC):
#     def __init__(self, device = 'device'):
#         self.device = device
#     @abstractmethod
#     def turn_on(self):
#         return f'{self.device} is turned on'
    
# class Phone(ElectronicDevice):
#     def __init__(self, phone):
#         super().__init__(phone)
    
#     def turn_on(self):
#         return super().turn_on()
    
#     def turn_off(self):
#         return f'{self.device} is turned off'
    
# class Laptop(ElectronicDevice):
#     def __init__(self, laptop):
#         super().__init__(laptop)
    
#     def turn_on(self):
#         return super().turn_on()
    
#     def turn_off(self):
#         return f'{self.device} is turned off'

    
# obj = Phone('Iphone 16')
# print(obj.turn_on())
# obj1 = Laptop('Asus')
# print(obj1.turn_off())

# class Person(ABC):
#     @abstractmethod
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @abstractmethod
#     def get_info(self):
#         return f'Name - {self.name} and age - {self.age}'
    
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def get_info(self):
#         return super().get_info() + '- Student'
    
# class Teacher(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def get_info(self):
#         return super().get_info() + '- Teacher'
    
# obj = Student('Graf', 16)
# obj1 = Teacher('Gercog', 56)
# print(obj.get_info())
# print(obj1.get_info())

# class PaymentMethod(ABC):
#     @abstractmethod
#     def __init__(self, method = 'method'):
#         self.method = method

#     @abstractmethod
#     def procces_payment(self):
#         return f'Thank you for using {self.method}'
    
# class Paypal(PaymentMethod):
#     def __init__(self, method):
#         super().__init__(method)
    
#     def procces_payment(self):
#         return super().procces_payment()
    
# class CreditCard(PaymentMethod):
#     def __init__(self, method):
#         super().__init__(method)
    
#     def procces_payment(self):
#         return super().procces_payment()
    
# obj = Paypal('Paypal')
# obj1 = CreditCard('Visa')
# print(obj.procces_payment())
# print(obj1.procces_payment())



# class Document(ABC):
#     @abstractmethod
#     def __init__(self, document = 'document'):
#         self.doc = document

#     @abstractmethod
#     def open(self):
#         return f'{self.doc} is opened'
    
#     @abstractmethod
#     def save(self):
#         return f'{self.doc} is saved'
    
#     @abstractmethod
#     def close(self):
#         return f'{self.doc} is closed'


# class WordDocument(Document):
#     def __init__(self, document='Word'):
#         super().__init__(document)
#     def open(self):
#         return super().open()
    
#     def save(self):
#         return super().save()
    
#     def close(self):
#         return super().close()


# class PDF(Document):
#     def __init__(self, document='PDF'):
#         super().__init__(document)
#     def open(self):
#         return super().open()
    
#     def save(self):
#         return super().save()
    
#     def close(self):
#         return super().close()

# obj = WordDocument()
# print(obj.open())
# print(obj.save())
# obj1 = PDF()
# print(obj1.close())

