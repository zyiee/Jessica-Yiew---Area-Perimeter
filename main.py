shapes = ['Rectangle','rectangle', 'Circle', 'circle', 'Triangle','triangle', 'Square', 'square','Parallelogram', 'parallelogram'] #list of shapes available to calculate
calc_type = ['Area', 'area', 'Perimeter', 'perimeter'] #area and perimeter options
rectangles = [shapes[0], shapes[1]]
circles = [shapes[2], shapes[3]]
triangles = [shapes[4], shapes[5]]
squares = [shapes[6], shapes[7]]
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

def app_dictionary(x):
    global results
    results = [op1, x]
    history[op2] = results

def rec_function():
    rec_dimensions() 
    if op1 in area:
        area_r = r_base*r_height
        print('Area of rectangle:', area_r)
        app_dictionary(area_r)
    elif op1 in perimeter:
        perimeter_r = (2*r_base)+(2*r_height)
        print('Perimeter of rectangle:', perimeter_r)
        app_dictionary(perimeter_r)

if op2 in rectangles:        
  rec_function()
  print(history)
#--------------------------circle----------------------------
def circ_length():
  global circ_radius
  print('Circle radius is half of diameter length.')
  while True:
    try:
      circ_radius = int(input('What is the radius of your circle?\t'))
      break
    except ValueError:
      print('Please enter a number value.')
  print('Radius length:', circ_radius)

pi = 3.141592

def circ_function():
  circ_length()
  if op1 in area:
    area_c = pi*(circ_radius**2)
    print('Area of circle:', area_c)
    app_dictionary(area_c)
  elif op1 in perimeter:
    perimeter_c = 2*pi*circ_radius
    print('Perimeter of circle:', perimeter_c)
    app_dictionary(perimeter_c)

if op2 in circles:
  circ_function()
  print(history)
#--------------------------triangle----------------------------
def tri_base():
  global t_base
  while True:
    try:
      t_base = int(input('Base length:\t'))
      break
    except ValueError:
      print('Please enter a number value.')

def tri_height():
  global t_height
  while True:
    try:
      t_height = int(input('Height length:\t'))
      break
    except ValueError:
      print('Please enter a number value.')

def tri_dimensions():
  print('What are the dimensions of your triangle?')
  tri_base()
  tri_height()
  print('Height value:', t_height, 'Base value:', t_base)

def tri_function():
  tri_dimensions()
  if op1 in area:
    area_t = 0.5*t_base*t_height
    print('Area of triangle:', area_t)
    app_dictionary(area_t)

if op2 in triangles:
  tri_function()
  print(history)
#--------------------------square----------------------------
def square_base():
    global sq_base
    while True:
        try:
            sq_base = int(input('Base length:\t'))
            break
        except ValueError:
            print('Please enter a number value.')

def square_height():
    global sq_height
    while True:
        try:
            sq_height = int(input('Height length:\t'))
            break
        except ValueError:
            print('Please enter a number value.')

def square_dimensions():
    print('What are the dimensions of your square?')
    square_base()
    square_height()
    print('Height value:', sq_height, 'Base value:', sq_base)

def square_function():
    square_dimensions() 
    if op1 in area:
        area_sq = sq_base*sq_height
        print('Area of square:', area_sq)
        app_dictionary(area_sq)
    elif op1 in perimeter:
        perimeter_sq = (2*sq_base)+(2*sq_height)
        print('Perimeter of rectangle:', perimeter_sq)
        app_dictionary(perimeter_sq)

if op2 in squares:        
  square_function()
  print(history)