class PlayerCharacter:
    membership = True  # Class object attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    @classmethod
    # Tukaj moramo dodati parameter cls. To je za objekte isto kot za metode self
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    # Tukaj pri statičnih metodah pa nimamo dostopa do cls (objekta)
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Mujo', 41)

print(player1.membership)
print(player1.name)
print(player1.run())
print(player1.age)
print(player1.adding_things(2, 3))


class Test:
    x = 10

    def __init__(self) -> None: # __DunderMethod__
        self.x = 20

    def get_name(self, name):
        return(name)


test = Test()
print(test.x)
print(Test.x)
print(test.get_name('Mujo'))

username = 'Mujocitoo'
print(len(username))
