class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # print(args)
        # print(kwargs)
        # print(args[0])
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")



    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(self.houses_history)
        # help(type(self))

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

    fundament = True


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('ЖК Матрёшки', 20)

del(h1)
del(h2)
print(House.houses_history)