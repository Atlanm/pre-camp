para_length = int(input('Please enter your Parallelogram length: '))
para_height = int(input('Please enter your Parallelogram height: '))

for line in range(para_height):
    if (line == para_height-1) or (line == 0):
        print(' '*(para_height-line), '* '*para_length)
    else:
        print(' '*(para_height-line), '* ', '  '*(para_length-3), '*')
