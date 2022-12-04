
# Program 1, first and last name separate input
# first_name = input('Enter your first Name: ')
# last_name = input('Enter your last name: ')
# print(first_name + "." + last_name + '@gmail.com')


# Program 2, Only one input
full_name = input("Enter your full name: ")
list_name = full_name.split()
print(list_name)
first_name = list_name[0]
print(first_name)
last_name = list_name[1]
print(last_name)
print(first_name + "." + last_name + '@ihsmarkit.com')
