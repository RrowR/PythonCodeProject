class Neko:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def sleep(self, position):
        print(f"{self.name}这只{self.sex}猫正在{position}休息")

    def eat(self, food):
        print(f"{self.name}这只{self.sex}猫正在吃{food}")


neko1 = Neko("猫羽雫", "母")
neko1.sleep("地板上")
neko1.eat("饭")
