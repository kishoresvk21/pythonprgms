class Classy:
    varia = 1
    def __init__(self):
        self.var = 2
        self.me=677
        self.o=99

    def method(self):
        pass

    def __hidden(self):
        pass

obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)
