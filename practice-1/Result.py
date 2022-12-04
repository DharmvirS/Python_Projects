def voting_age():
    a = int(input('Enter your Age: '))
    if a>=18:
        print('You are eligible for Voting')
    else:
        print('You are under-age hence not eligible for Voting')

# Write a program to calculate total marks in 5 subjects(Full Marks = 100) as well as percentage of marks and division as per the following condition: percentage >= 80 - Grade A,
# Percentage >= 60 - Grade B, Percentage >= 40 - Grade C   Percentage <40 - Grade D

import sys
def valid_marks_input(num):
    if not 0 <= num <= 100:
        print('Marks should be between 0-100')
        return False
def result():
    i = 5
    final_marks = 0
    while i:
        a= float(input('Enter '+str(i)+'th Subject Marks: '))
        check_num = valid_marks_input(a)
        if check_num is False:
            sys.exit()
        final_marks = final_marks + a
        i = i-1
    print('Total Marks: ',final_marks)
    final_marks = final_marks/5
    print('Percentage: ',final_marks,'%')
    if  final_marks >=80 :
        print('Grade A')
    elif final_marks >= 60 and final_marks <80:
        print('Grade B')
    elif final_marks >=40 and final_marks<60 :
        print('Grade C')
    else:
        print('Grade D')

    # a= float(input('Enter 1st Subject Marks: '))
    # valid_marks_input(a)
    # b=float(input('Enter 2nd Subject Marks: '))
    # valid_marks_input(b)
    # c=float(input('Enter 3rd Subject Marks: '))
    # valid_marks_input(c)
    # d=float(input('Enter 4th Subject Marks: '))
    # valid_marks_input(d)10
    # e=float(input('Enter 5th Subject Marks: '))
    # valid_marks_input(e)
    # print('Total Marks: ',(a+b+c+d+e))

    # if not 0 <= a <= 100:
    #     print('Max marks can be 100')
    # if not 0 <= b <= 100:
    #         print('Max marks can be 100')
    # if not 0 <= b <= 100:
    #         print('Max marks can be 100')
    #
    #

result()
