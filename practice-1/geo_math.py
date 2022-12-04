#def is used to make it as function
def geometry():
    print('Whose Area and Perimeter you want to know : Rectangle, Square, Circle.')
    c = input()
    if c == 'Rectangle':
        a = int(input('Enter Length= '))
        b = int(input('Enter Breadth = '))
        print('Area of Rectangle =', a * b)
        print('Perimeter of Rectangle =',2*a+2*b)
    elif c == 'Square':
        a = int(input('Enter side= '))
        print('Area of Square =',a**2)
        print('Perimeter of Square =',4*a)
    elif c == 'Circle':
        r = float(input('Enter Radius = '))
        print('Area of Circle =',22/7*r**2)
        print('Circumference of Circle =', 2*22/7*r)
    else:
        print('Error, Choose your choice wisely OR Check your Spell one more time')


if __name__ == '__main__': #It should be made as in any program when you call this function/file, that program would always be main.
    geometry()