# Inheritance

class User():
    def sign_in(self):
        print("Logged in")

# Children classes or subclasses or derived classes


class Wizard(User):
    def __init__(self, name, power) -> None:
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows) -> None:
        self.name = name
        self.num_arrows = num_arrows

    def display_name(self):
        print(self.name)

    def attack(self):
        print(f'attacking with arrows: Arrows left: {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
archer2 = Archer('TheHood', 22)
print(wizard1.sign_in())
wizard1.attack()
archer1.attack()
archer2.sign_in()
print(archer2.display_name())

print(isinstance(archer1, Archer))
