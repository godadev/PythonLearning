while True:
    try:
        age = int(input('What is your age?'))
        10 / age
    except ValueError:
        print('Please enter a number:')
    except ZeroDivisionError:
        print('You can\'t be 0 years old. Please enter a number:')
    else:
        print('Thank You.')
        break
