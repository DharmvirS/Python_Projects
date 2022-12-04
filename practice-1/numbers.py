#Repeat 10 times whatever you want to Type:
def repeat():
    i=1
    n=input('Type whatever you want to repeat 10 times: ')
    while(i<=10):
        print(n)
        i=i+1
# Program to print first 10 natural numbers starting from the user input:
def nat_num():
    n=int(input('Provide your number from where you want to get first 10 Natural Numbers: '))
    i=n
    while(i<=n+9):

        i=i+1
        print(i)
# Program from n to 1 (counting in reverse order from user's input)
def reverse():
    n=int(input('Enter your number: '))
    while(n):
        print(n)
        n = n-1
# Program to find sum of 1 to n
def sum():
    n= int(input('Enter number upto which you want the Sum: ' ))
    sum = 0
    i = 1
    while(i<=n):
        sum=sum+i
        i=i+1
        print(sum)

#Program to find sum of Square from 1 to n numbers
def sum_square():
    n=int(input('Enter the number upto which you want sum of square: '))
    i=1
    sum=0
    while(i<=n):
        sum=sum+(i*i)
        i=i+1
        print(sum)
# program for leap year
def leap_year():
    year = int(input())
    if year%4==0:
        print('True')
    else:
        print('False')

#sum of sqaure from 1 to n
def sum_of_Square():
    n=int(input('Enter your number: '))
    i=1
    sum = 0
    while (i<=n):
        sum=(sum+i**2)
        i=i+1
        print('Sum= ',sum)

#sum of only even numbers upto n
def add_of_even():
    n=int(input('Enter the number upto where you want to add even number:  '))
    i=2
    sum=0
    while(i<=n):
        sum=sum+i
        i=i+2
    print('Total: ',sum)
add_of_even()

# Program for sum of digit
def sum_of_digit():
    i=int(input('Enter the number whose digit sum you want: '))
    sum=0
    while(i>0):
        sum=sum+i%10
        i=i//10
    print('Sum of digit= ',sum)
sum_of_digit()
