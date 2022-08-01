def generator_func():
    yield 1
    yield 2
    yield 5
    yield 6
    yield 8
    yield 9
    raise StopIteration

gen = generator_func()

for i in gen:
    print(i)
    if i == 2:
        break

print('---')

print(next(gen))
print(next(gen))

print('---')

print(gen.send(None))
print(gen.send(None))

