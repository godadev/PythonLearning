my_list = [char for char in 'Welcome to my city']

print(my_list)

my_int_list = [item for item in range(100)]
print(my_int_list)
my_int_list = [item for item in range(100) if item < 5]
print(f'This are the items {my_int_list}')
my_int_list = [num ** 2 for num in range(100)]
print(my_int_list)

# set and dictionary comprehensions is basically the same as list comprehension

# Create a quick dictionary from a list
my_dict = {num: num * 2 for num in my_int_list}
print(my_dict)
