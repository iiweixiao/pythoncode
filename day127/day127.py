class Test:
    def __init__(self, str):
        self.str = str

    def func(self):  # 普通函数，是function
        print(f'我是普通的实例方法，传参是{self.str}')

    @staticmethod
    def static_method():  # 静态方法，是function
        print(f'我是静态方法，没有传参')

    @classmethod
    def class_method(cls, str1):  # 类方法，是method
        print(f'我是类方法，传参是{str1}')


def func1():
    print(f'我是普通方法，没有传参')


t1 = Test(str='str')

# 1. 普通的实例方法
t1.func()
Test.func(t1)  # 与上一样
print(type(t1.func))  # <class 'method'>

# 2. 静态方法，在定义时，不需要 self 参数
t1.static_method()
Test.static_method()  # 与上一样
print(type(t1.static_method))  # <class 'function'>

# 3. 类方法，在定义时，第一个参数固定是 cls，为 class 的简写，代表类本身。不管是通过实例还 是类调用类方法，都不需要传入 cls 的参数。
t1.class_method('str1')
Test.class_method('str1')
print(type(t1.class_method))  # <class 'method'>

# 4. 普通函数
func1()
print(type(func1))  # <class 'function'>