import utility
import shopping.shop
import random

# if __name__ == '__main__':
#     print(utility.multiply(2, 4))
#
#     print(utility.divide(2, 345))
#
#     print(shopping.shop.buy('apple'))

print(random.random())
print(random.randint(1, 22))
print(random.choice([1, 3, 6, 3, 2, 6, 77]))
shuffle_list = [1, 1, 2, 3, 4, 1, 2, 3, 21]
random.shuffle(shuffle_list)
print(shuffle_list)
