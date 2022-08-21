class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name}跑起来啦")

    @staticmethod
    def eat():
        print("正在吃饭..")

    @classmethod
    def jump(cls, name):
        print(f"{name}跳起来啦")


def demo_func():
    ...

dog = Animal(name='小黑')

dog.run()
Animal.run(dog)

dog.eat()
Animal.eat()

dog.jump('小白')
Animal.jump('小白')

print(type(demo_func))
print(type(dog.run))
print(type(dog.eat))
print(type(dog.jump))

