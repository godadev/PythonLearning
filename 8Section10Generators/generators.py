from time import time
# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result
#
#
# my_list = make_list(100)
# print(my_list)


# -----------------------------------------
# Generator

def generator(num):
    t1 = time()
    for i in range(num):
        print(f'Start time {t1}')
        yield i * 4
        t2 = time()
        print(f'End time {t2}')
        print(t2 - t1)


for item in generator(10):
    print(item)



