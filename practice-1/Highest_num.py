# Program to find highest number between two given number
def greater_num():
    a= float(input('Enter First Number: '))
    b= float(input('Enter Second Number: '))
    if a>b:
        print('First Number is greater than Second Number')
    elif a==b:
        print('Both are Equal')
    else:
        print('Second Number is greater than First Number')

def check_highest_num():
    # Program to find highest num between three numbers

    a=float(input('Enter 1st number = '))
    b=float(input('Enter 2nd number = '))
    c=float(input('Enter 3rd number = '))
    if a>b:
        print('1st number is the Highest')
    elif b>c:
        print('2nd number is the Highest')
    else:
        print('3rd number is the Highest')

check_highest_num()
def check_negative():
    #check whether input is +ve,-ve or zero
    a=float(input('Enter your number: '))
    if a>0:
        print('Number is Positive')
    elif a<0:
        print('Number is Negative')
    else:
        print('Number is Zero')


#find a middle number in a group of three numbers
def mid_num():
    a=int(input('Enter 1st number: '))
    b=int(input('Enter 2nd number: '))
    c=int(input('Enter 3rd number: '))
    if (a>b and a<c) or (a<b and a>c):
        print('Middle number = ',a)
    elif (b>c and b<a) or (b<c and b>a):
        print('Middle number = ',b)
    else:
        print('Middle number = ',c)
