def fun(top=5):
    index = 0
    while index < top:
        print(f'index={index}')
        index += 1
        yield index
    raise StopIteration

gen = fun()
gen.send(None)
gen.send(None)
gen.send(None)
next(gen)
next(gen)
