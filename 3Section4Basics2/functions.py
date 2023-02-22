# %% [markdown]
# ### Functions

# %%
def say_hello(name):
    print(f'Hello {name}')


name = input('Tell us your name please: ')
say_hello(name)

# %%


def sum(num1, num2):
    return (num1 + num2)


mytotal = sum(4, 5)
print(mytotal + 100)
print(sum(mytotal, mytotal))

# %% [markdown]
# ### Methods VS Functions
# Metode se kličejo na objektih in jih moramo tako tudi klicati.<br>
# Naprimer:

# %%


class ABC:
    def method_abc(self):
        print("I am in method_abc of ABC class. ")


class_ref = ABC()  # object of ABC class
class_ref.method_abc()

# ---------------------------------------------------------------------------------------------
# mylist je objekt tipa list, ki je vgrajen v Python, zato na njem lahko pokličemo metode.
mylist = [1, 2, 3, 4, 5]
mylist.reverse()
print(mylist)

# %% [markdown]
# ### Docstrings

# %%


def test(a, b):
    """Function to sum a and b

    Args:
        a (integer): First number
        b (integer): Second number
    """

    print(a + b)


test(1, 3)

# %% [markdown]
# ### Lambda functions

# %%


def x(a, b): return a * b


print(x(5, 6))


def my_lambda(a, b, c, d): return a * b - c / d


print(my_lambda(2, 3, 4, 7))


def my_printed_lambda(a): return a


print(my_printed_lambda('Hello: '))

# %% [markdown]
# ### *args and **kwargs

# %%


def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():  # **kwargs dostopamo samo z zanko ker predsatvljajo key:value par
        total += items
    return sum(args) + total


super_func(1, 3, 4, num1=3, num2=45)


# %% [markdown]
# ### Functions exercise

# %%
#   Moja rešitev

def highest_even_func(li):
    highest_even_num = 0
    for items in li:
        if (items % 2) == 0:
            if (items > highest_even_num):
                highest_even_num = items
    print("The highest even number is:" + str(highest_even_num))


print(highest_even_func([10, 2, 3, 5, 6, 8, 11, 23, 25, 24, 28, 100]))

#   Rešitev, ki je bila v vajah


def highest_even(num):
    evens = []
    for item in num:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


my_highest_list = [10, 2, 3, 5, 6, 8, 11, 23, 25, 24, 28, 100]

print(highest_even(my_highest_list))

# %% [markdown]
# ### Walrus operator :=

# %%
a = "Hellooooo"

if((n := len(a)) > 5):
    print(f"The string has {n} characters and is to long.")


while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]
    print(a)


# %% [markdown]
# ### Scope

# %%
name = '   mujo '
print(name)  # Spremenljivka ne obstaja
x = int(5)
print(x)
print(type(x))
print(name.strip())
print(name.upper())
print(name.replace("m", "b"))

test = "Hello"[0]
numa = name
print(numa)

x = ("apple", "banana", "cherry")
print(type(x))

txt = "Hello World"
x = txt[2:5]
print(x)
print(bool("abc"))
