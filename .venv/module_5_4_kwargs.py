class House:
    houses_history = []

    def __new__(cls, **kwargs):
        cls.houses_history.append(kwargs['name'])
        return object.__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k,  v)

        # self.name = name
        # self.number_of_floors = number_of_floors
        print(self.houses_history)
        # help(type(self))


jk1 = {'name' : 'ЖК Эльбрус', 'number_of_floors' : 10}
jk2 = {'name' : 'ЖК Акация', 'number_of_floors' : 20}
jk3 = {'name' : 'ЖК Матрёшки', 'number_of_floors' : 30}

h1 = House(**jk1)
h2 = House(**jk2)
h3 = House(**jk3)

del (h1)
del (h2)
print(House.houses_history)
