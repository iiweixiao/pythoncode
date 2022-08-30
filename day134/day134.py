from functools import singledispatch


@singledispatch
def age(obj):
    print('请传入合法类型的参数！')


@age.register(int)
def _(age):
    print('我已经{}岁了。'.format(age))


@age.register(str)
def _(age):
    print('I am {} years old.'.format(age))


@age.register(dict)
def _(age):
    print('hahah')


@age.register(list)
def _(age):
    print('hahah')


age(23)  # int
age('twenty three')  # str
age(['23'])  # list
