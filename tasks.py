# # class Bank:
# #     def __init__(self) -> None:
# #         self.money = 0

# #     def take(self, money) -> None:
# #         self.money += money
# #         print(self.money)
# #     def give(self, money) -> None:
# #         self.money -= money
# #         print(self.money)
# #     def show(self) -> None:
# #         print(self.money)
    
# # obj = Bank()
# # print(obj.take(200))
# # print(obj.take(200))
# # print(obj.give(350))
# # print(obj.take(1000))
# # print(obj.show())

# class Song:
#     def __init__(self, author, title, year) -> None:
#         self.author = author
#         self.title = title
#         self.year = year

#     def showauthor(self) -> None:
#         return f'Автором является: {self.author}'
    
#     def showtitle(self) -> None:
#         return f'Название - {self.title}'
    
#     def showyear(self) -> None:
#         return f'Год выхода - {self.year}'
    
# obj = Song('Kendrick', 'i', '2014')
# print(obj.showauthor())
# print(obj.showtitle())
# print(obj.showyear())



# class Bankaccount:
#     def __init__(self, balance) -> None:
#         self.balance = balance
    
#     def withdraw(self, money) -> None:
#         self.balance += money
#         return f'Текущий баланс {self.balance}'
#     def deposit(self, money) -> None:
#         self.balance -= money
#         return f'Текущий баланс {self.balance}'

# obj = Bankaccount(0)
# print(obj.withdraw(100))
# print(obj.withdraw(100))
# print(obj.deposit(50))
    

# class Taxi:
#     def __init__(self, name, cost, cost_km) -> None:
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self) -> None:
#         print(f'Расстояние - {self.cost_km}')
#         print(f'Цена - {self.cost}')
#         print(f'Название - {self.name}')

# obj = Taxi('Porsche', '1000', '90')
# print(obj.get_total_cost())


# class Phone:
#     def __init__(self, name, last_name, phone) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self) -> None:
#         print(f'Имя - {self.name}')
#         print(f'Фамилия - {self.last_name}')
#         print(f'Номер телефона - {self.phone}')

# obj = Phone('Stephen', 'Curry', '996500843015')
# print(obj.get_info())


# class Salary:
#     def __init__(self, percent) -> None:
#         self.percent = percent

#     def gnit(self, salary, experience) -> None:
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self) -> None:
#         self.salary = self.salary * 0.08
#         return self.salary

# obj = Salary(8)
# print(obj.gnit(150000, 1))
# print(obj.count_percent())


