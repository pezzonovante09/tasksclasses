"""
Наследование - принцип ООП, в котором мы можем унаследовать, переопределить и использовать в дочернем классе все аттрибуты и методы из родительского класса
"""


# class A:
#     def method(self):
#         print('Метод в классе А')

# obj_a = A()
# obj_a.method()

# class B(A):
#     """
#     Наследовали все методы и аттрибуты у класса А
#     """


# class C(B):
#     """
#     Наследовали все методы и аттрибуты у класса B (который наследуется от класса А)
#     и переопределили метод method
#     """
#     def method(self):
#         print('Метод в классе C')

#     """
#     метод method_c есть только у класса С, и отношения к классу B и A он никакого не имеет
#     """
#     def method_c(self):
#         print('Я метод')


# obj_b = B()
# obj_b.method()
# obj_c = C()
# obj_c.method()
# obj_c.method_c()


# class A:
#     x = 'x in A'
#     y = 'y in A'


# class B(A):
#     x = 'x in B'

# print(A.x)
# print(A.y)
# print(B.x)
# print(B.y)
"""
x in A
y in A
x in B
y in A
"""

"""
MRO - Method resolution order - Порядок поиска аттрибутов
"""
# print(B.mro())
# [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# obj = B()

# print(dir(object))['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
print('-------------------------')
# print(dir(obj))['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'x', 'y']


class A:
    def my_range(self, n):
        return list(range(n+1))

obj = A()
# print(obj.my_range(10))

# print(A().my_range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# class B(A):
#     def my_range(self, n):
#         # через super() мы обращаемся к родительскому классу и вызываем метод
#         print(list(range(n-1)))
#         return super().my_range(n)
    
# obj_b = B()
# obj_b.my_range(10)
# print(obj_b.my_range(10))

"===========================================Виды наследования================================="
"""
1) Одиночное наследование - это когда мы наследуемся в дочернем классе только от 1 класса
2) Множественное наследование - это когда мы в дочернем классе наследуемся от нескольких классов
3) Многоуровневое наследование - это когда мы наследуемся от класса у которого есть родитель
4) Иерархическое наследование - это когда от одного родителя много дочерних классов
5) Гибридное наследование - это когда используются несколько видов наследования
"""
"=======================================Множественное наследование================================"
# class A:
#     a = 'a'


# class B:
#     b = 'b'


# class C(A, B):
#     '''
#     Насдедовали все аттрибуты и методы у классов А и В
#     '''
#     c = 'c'

# obj_c = C()
# print(obj_c.a) # a
# print(obj_c.b) # b
# print(obj_c.c) # c


# class A:
#     def method(self):
#         print('метод в классе А')


# class B:
#     def method(self):
#         print('метод в классе В')


# class C(A, B):
#     ...


# obj_c = C()
# obj_c.method() # метод в классе А
# print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
"============================Проблемы множественного наследования======================"
# Проблема ромба (решена при помощи MRO)
# class A:
#     def method(self):
#         print('метод в классе А')


# class B:
#     def method(self):
#         print('метод в классе В')


# class C(A, B):
#     ...

"""
Проблема перекрестного наследования (не решена)
"""

class A:
    a = 'a'


class B:
    b = 'b'


class D(A, B):
    ...


class E(B, A):
    ...

class F(D, E):
    ...

obj_f = F()
print(obj_f.a)
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B