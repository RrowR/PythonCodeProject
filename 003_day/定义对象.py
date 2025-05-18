class Cat:
    def __init__(self):  # 构造方法定义属性
        self.names = "猫"

    def speak(self, mind):
        print(self.names + "speak" + mind)


neko1 = Cat()
print(neko1.names)


class Dog:
    def __init__(self, name):  # 构造方法传入定义属性
        self.names = name


neko1 = Cat()

print(neko1.names)
neko1.speak("你好")

dog1 = Dog("旺财")
print(dog1.names)

# class Student:
#     def __init__(self, name, stu_no, chinese, math, english):
#         self.name = name
#         self.stu_no = stu_no
#         self.chinese = chinese
#         self.math = math
#         self.english = english
#
#     def getInfo(self):
#         print(self.name + " 的学号是：" + str(self.stu_no) + " 语文成绩是：" + str(self.chinese) + " 数学成绩是：" + str(self.math) + "英语成绩是：" + str(self.english))
#
#
# Student("张三", 1, 12, 22, 22).getInfo()
# Student("张四", 2, 33, 12, 35).getInfo()
# Student("张五", 3, 44, 51, 31).getInfo()


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


# 优化版本
class Student:
    def __init__(self, name, stu_no):
        self.name = name
        self.stu_no = stu_no
        # 这里分数可以用字典
        self.grade = {"语文": 0, "数学": 0, "英语": 0}

    def getInfo(self):
        print(self.name + " 的学号是：" + str(self.stu_no) + self.grade)

    def setGrade(self, course, score):
        if course in self.grade:
            self.grade[course] = score

    def print_grade(self):
        print(f"学生{self.name}（学号:{self.stu_no}）的成绩为：")
        for course in self.grade:
            print(f"{course}:{self.grade[course]}分")


s1 = Student("张三", 111)
s1.setGrade("语文", 87)
s1.setGrade("数学", 88)
s1.setGrade("英语", 121)

s1.print_grade()
