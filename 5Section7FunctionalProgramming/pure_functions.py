from functools import reduce

item_list = [1, 2, 3, 4, 5, 6]
list_to_add = [6, 77, 78, 45, 23]


def multiply_by2(li):
    # pri map funkciji ne potrbujemo več te inicializacije polja (list)
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2(item_list))

# map(), filter(), zip(), reduce()

# map()


def multiply_by2_new(item):
    return item * 2


print(list(map(multiply_by2_new, item_list)))

# filter()


def check_if_odd(item):
    return item % 2 != 0


print(list(filter(check_if_odd, item_list)))
print(item_list)  # Ne spremeni originalnih podatkov

# zip()
print(list(zip(item_list, list_to_add)))

# reduce()


# lambda expressions
print(list(map(lambda item: item * 2, item_list)))


def test_item(my_item): return my_item * 3


print(test_item(8))


def x(a): return a * a


print(x(1))


# Exercises
# power ** lambda
my_list = [5, 4, 3]
new_list = list(map(lambda num: num ** 2, my_list))
print(new_list)

# List sorting lambda
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

a.sort(key=lambda x: x)
print(a)
