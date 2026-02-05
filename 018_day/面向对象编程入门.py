class Student:

    def study(self, course_name):
        print(f"学生正在学习{course_name}")

    def sleep(self):
        print("学生正在睡觉")


stu1 = Student()
stu2 = Student()
print(stu1)    # <__main__.Student object at 0x10ad5ac50>
print(stu2)    # <__main__.Student object at 0x10ad5acd0>
print(id(stu1),id(stu2))
print(hex(id(stu1)), hex(id(stu2)))    # 0x10ad5ac50 0x10ad5acd0

Student.study(stu1,"Python程序设计")
stu1.study("C++程序设计")

Student.sleep(stu2)
stu2.sleep()



