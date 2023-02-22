import pandas as pnd
import numpy as np

print(pnd.__version__)
print(np.__version__)

myname = input('Please enter your name: ')

if myname == 'Mujo':
    print('Length of the name is: ' + (str(len(myname))))
else:
    print('Your name doesnt match: ')