class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название {self.name}, количество этажей {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    # ==
    def __eq__(self, other):
        if self.number_of_floors == other.number_of_floors:
            return True
        else:
            return False

    # !=
    def __ne__(self, other):
        if self.number_of_floors != other.number_of_floors:
            return True
        else:
            return False

    # <
    def __lt__(self, other):
        if self.number_of_floors < other.number_of_floors:
            return True
        else:
            return False

    # <=
    def __le__(self, other):
        if self.number_of_floors <= other.number_of_floors:
            return True
        else:
            return False

    # >
    def __gt__(self, other):
        if self.number_of_floors > other.number_of_floors:
            return True
        else:
            return False

    # >=
    def __ge__(self, other):
        if self.number_of_floors >= other.number_of_floors:
            return True
        else:
            return False

    # +
    def __add__(self, x):
        self.number_of_floors = self.number_of_floors + x
        return self

    # x + object.argument
    def __radd__(self, y):
        self.number_of_floors = int(y) + self.number_of_floors
        return self

    # +=
    def __iadd__(self, y):
        self.number_of_floors += y
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)

print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__



