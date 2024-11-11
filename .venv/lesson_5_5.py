class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    head = True

den = Human('Денис', 22)
max = Human('Макс', 23)

print(den.__dict__)
