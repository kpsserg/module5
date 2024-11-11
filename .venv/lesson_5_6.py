class User:
    def __init__(self, *args, **kwargs):
        self.args = args
        for key, value in kwargs.items():
            setattr(self, key, value)

other = [1, 2, 3]
user = {'name' : 'Den', 'age' : 25, 'gender' : 'male'}
user1 = User(*other, **user)

print(user1.args)
print(user1.name)
print(user1.age)
print(user1.gender)