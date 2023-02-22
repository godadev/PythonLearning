try:
    with open('test1.txt', mode='w') as my_file:  # Read and write
        text = my_file.write('Hello from Python ')
        print(my_file.read())
except FileNotFoundError as err:
    print('File does not exist')
    raise err

# a parameter = append mode
# w parameter = write / also creates a file if it doesnt exist
# r parameter = read mode
# r+

# File paths
