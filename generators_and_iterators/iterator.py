class Squares(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current


iterator = Squares(1, 5)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# for square in Squares(1, 5):
#     print(square)

iterator = Squares(1, 5)
for square in Squares(1, 5):
    print(square)
