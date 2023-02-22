# @classmethod
# @staticmethod

def hello():
    print('Helloooo!')


greet = hello()
print(greet)

# Make our own @decorator


def my_decorator(func):
    def wrap_func():
        print('*********************')
        func()
        print('*********************')
    return wrap_func


@my_decorator
def hello():
    print('Hello')


@my_decorator
def bye():
    print('See you all later! GoodBye!')


hello()
bye()
