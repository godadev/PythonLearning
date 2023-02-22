class Pets():
    animals = []

    def __init__(self, animals) -> None:
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking arround'


class Simon(Cat):
    def sing(self, sounds):
        return f'{self.name} goes {sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Niko(Cat):
    def sing(self, sounds):
        return f'{sounds}'


my_cats = [Simon('Piki', 3), Sally('Muc', 5), Niko('Bimbo', 6)]

my_pets = Pets(my_cats)

my_pets.walk()
print(my_pets.animals[0].sing('mooo'))

print(dir(Pets))
