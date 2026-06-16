class Student:
    # __slots__ = ('name','age')   限制动态改变对象属性
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self):
        print(f'{self.__age}的{self.__name}正在吃蛋糕')

s1 = Student('猫羽雫',18)
s1.study()
# print(s1.__name)       AttributeError: 'Student' object has no attribute '__name'
s1.sex = '女'
















