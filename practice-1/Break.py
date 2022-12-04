# from exiting this loop system (continuously asking for name), we use BREAK Statement
Name = input('Enter your Full Name: ')
while True :
    if Name == 'Dharmvir Singh':
        break
    Name != 'Dharmvir Singh'
    print('You are not authorised !!')
    Name = input('Enter your name again : ')

print('Access Granted, Thank You!!!')