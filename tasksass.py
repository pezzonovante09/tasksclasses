# class Address:
#     def __init__(self, street, city, country):
#         self.street = street
#         self.city = city
#         self.country = country

#     def __str__(self):
#         return 'gyat'
    
# class Person:
#     def __init__(self, street, city, country):
#         self.address = Address(street, city, country)

#     def __str__(self):
#         return f'{self.address}'

# a = Person('Tokombaeva', 'Bishkek', 'Kyrgyzstan')
# print(a)
# del a

# class School:
#     def __init__(self, name):
#         self.name = name
#         self.students = []

#     def add_student(self, student):
#         self.student = student
#         self.students.append(student)

#     def show_student(self):
#         print(f"Students in {self.name}:")
#         for student in self.students:
#             print(student.name)
    
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.school = []

# a = School('61')
# b = School('9')
# student1 = Student('Graf')
# student2 = Student('Pork')
# a.add_student(student1)
# a.add_student(student2)
# b.add_student(student1)

# print(a.show_student())
# print(b.show_student())

# class Mouse:
#     def __init__(self, model):
#         self.model = model
    
#     def __str__(self):
#         return f'{self.model}'

# class Computer:
#     def __init__(self, mouse, connected):
#         self.mouse = mouse
#         self.connection = connected

#     def check_mouse(self):
#         if self.connection == True:
#             return f'{self.mouse} is connected'
#         else:
#             return f"{self.mouse} isn't connected"
        
# mouse1 = Mouse('Logitech')
# mouse2 = Mouse('Sven')
# con1 = Computer(mouse1, True)
# con2 = Computer(mouse2, False)

# print(con1.check_mouse())
# print(con2.check_mouse())

# class Room:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

# class House:
#     def __init__(self):
#         self.rooms = []

#     def add_rooms(self, name):
#         self.room = Room(name)
#         self.rooms.append(self.room)
#         return f'{self.rooms}'
    
#     def count_rooms(self):
#         return len(self.rooms)
    

    
# a = Room('Зал')
# b = Room('Кухня')
# obj = House()
# print(obj.add_rooms(a))
# print(obj.count_rooms())
# print(obj.add_rooms(b))
# print(obj.count_rooms())

class Engine:
    def __init__(self, have):
        self.have = have

class Car:
    def __init__(self, have):
        self.engine = Engine(have)

    def start(self):
        if self.engine:
            return f'You can drive'
        else:
            return f'You cant drive'
        
a = Engine(True)
obj = Car(a)
print(obj.start())

