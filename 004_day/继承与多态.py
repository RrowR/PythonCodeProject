class Animal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


class Human(Animal):
    def __init__(self, name, sex, hobby):
        super().__init__(name, sex)
        self.hobby = hobby

    def play(self):
        print(self.name + "性别" + self.sex + "在" + self.hobby)


zhangsan = Human("猫羽雫", "女", "玩")
zhangsan.play()
