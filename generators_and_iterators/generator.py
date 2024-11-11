def squares(start, stop):
    for i in range(start, stop):
        yield i * i

generator = squares(1, 5)

for square in generator:
    print(square)

# iterator expression
generator2 = (i * i for i in range(1, 5))

for square in generator2:
    print(square)