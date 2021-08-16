shapes = ['Rectangle','rectangle', 'Circle', 'circle', 'Triangle','triangle', 'Square', 'square','Parallelogram', 'parallelogram'] #list of shapes available to calculate
calc_type = ['Area', 'area', 'Perimeter', 'perimeter'] #area and perimeter options
rectangles = [shapes[0], shapes[1]]
area = [calc_type[0], calc_type[1]]
perimeter = [calc_type[2], calc_type[3]]
history = {}
#formulae


def a_p(): #asks user if area or perimeter is to be calculated
    global op1
    op1 = str(input('Welcome to the area perimeter calculator. \nWould you like to calculate the area or perimeter?\t'))
    if op1 not in calc_type:
        print('Please enter either area or perimeter.')
        a_p()
    else:
        print(op1, 'has been selected.')
a_p()

def s_s(): #asks user which shape to calculate
    global op2
    op2 = str(input('What shape would you like to calculate the ' + op1 + ' of?\nShapes available are: Rectangle, Circle, Triangle, Square, Parallelogram\n'))
    if op2 not in shapes:
        print('Please choose from the given list.')
        s_s()
    else:
        print(op2, 'has been selected.')
s_s()
#--------------------------rectangle----------------------------
def rec_base():
    global r_base
    while True:
        try:
            r_base = int(input('Base length:\t'))
            break
        except ValueError:
            print('Please enter a number value.')

def rec_height():
    global r_height
    while True:
        try:
            r_height = int(input('Height length:\t'))
            break
        except ValueError:
            print('Please enter a number value.')

def rec_dimensions():
    print('What are the dimensions of your rectangle?')
    rec_base()
    rec_height()
    print('Height value:', r_height, 'Base value:', r_base)

def rec_dictionary(x):
    results = op1, x
    history[op2] = results

def rec_function():
    if op2 in rectangles:
        rec_dimensions() 
    if op1 in area:
        area_r = r_base*r_height
        print('Area of rectangle:', area_r)
        rec_dictionary(area_r)
    elif op1 in perimeter:
        perimeter_r = (2*r_base)+(2*r_height)
        print('Perimeter of rectangle:', perimeter_r)
        
rec_function()
print(history)
#--------------------------circle----------------------------
