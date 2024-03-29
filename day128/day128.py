class Word(str):
    def __new__(cls, word):
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            print(word)
            word = word[:word.index(' ')]
            print(word)
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)


w = Word('hd h dhd')
print(w.__lt__('h'))