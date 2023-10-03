from random import *
a=[0]*30
for i in range (len(a)):
    a[i]=randint(0,100)
    print(a[i],end=' ')
print()
b=[0]*31
for j in range(1,len(b)):
    b[j]=j
SEN=-1
remove_number=randint(5,8)
for i in range(remove_number):
    rand_student = randint(1, 29)
    b[rand_student]=SEN
    a[rand_student]=SEN
new_list=[0]*(30-remove_number)
for j in range(30):
    if a[j]!= SEN:
     print(a[j],end=' ')
print()
print('\tRoll No\t\t\tMarks')
for j in range(30):
    if a[j]!=SEN:
     print(f'\t{a[j]}\t\t\t\t{b[j]}')

