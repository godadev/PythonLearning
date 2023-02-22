picture  = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

has_pixel = '*'
no_pixel = ' '
for row in picture:
    for pixel in row:
        if(pixel == 1):
            print(has_pixel, end='')
        else:
            print(no_pixel, end='')
    print('')   #Need a new line after each row in picture