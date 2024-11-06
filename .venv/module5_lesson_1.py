class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'Я {self.name}. У меня день рождения. Мне теперь {self.age}')


den = Human('Денис', 22)
max = Human('Максим', 22)

den.surname = 'Попов'
print(den.surname)

den.birthday()
