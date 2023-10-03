from random import*
a=[0]*12
print('Monthly Sales :',end=' ')
for i in range(len(a)):
    a[i]=randint(10,99)
    print(a[i],end=' ')
print()
print('Quarter 1 :',end=' ')
sum1=0
for j in range(3):
    print(a[j],end='')
    sum1+=a[j]
    if j==0:
        min=a[j]
    elif min>a[j]:
        min=a[j]
    if j==0:
        max=a[j]
    elif max<a[j]:
        max=a[j]
print(f'Min : {min} Max : {max}',end='\t')
avg1=sum1/3
print('Average',avg1)
