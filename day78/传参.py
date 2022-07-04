def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")

    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
        print("-" * 40)
    for kw in keywords:
        print('*'*40)
        print(kw, ":", keywords[kw])


# cheeseshop('da', 12, 43, '123', {'ee': ['ee1', 34], 'rr': 2}, haha='nihao', lala='hello')

cheeseshop("Limburger", "It's very runny, sir. ", "It's really very, VERY runny, sir.", shopkeeper="Michael Palin",
           client="John Cleese", sketch="Cheese Shop Sketch")
