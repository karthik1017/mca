class InterfIter:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        num = self.num
        sel.num += 2
        return num

for i in InterfIter():
    print(i)