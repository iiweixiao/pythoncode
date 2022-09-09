str1 = [1, 2, 3, 4, 5]
str1.reverse()
print(str1)

str2 = 'abc'
print(str2[::-1])


def my_reverse(str):
    if str == "":
        return str
    else:
        return my_reverse(str[1:]) + str[0]

print(my_reverse('abc'))


def func():
    return "ok",

print(func())

