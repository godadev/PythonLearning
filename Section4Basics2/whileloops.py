i = 0
my_list = [1, 4, 7, 4]

while i < 50:
    print(i)
    i += 1
else:
    print('Were done here.')

j = 0
while j < len(my_list):
    print(my_list[j])
    j += 1


while True:
    response = input('Tell us your name. ')
    if (response == 'bye'):
        break