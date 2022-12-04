from Table import table
from geo_math import geometry
from odd_even import number

i=1
sum=0
n=int(input('Enter the number upto which you want to add: '))
while(i<=n):
    sum=sum+i
    i=i+1
print('Your Total=',sum)
