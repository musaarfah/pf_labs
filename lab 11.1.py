from random import*
l=int(input('Length :'))
a=[0]*l
for i in range(len(a)):
    a[i]=randint(10,99)
    print(a[i],end=' ')
print()
b=[a[j] for j in range(len(a))]
c=[0]*10
for k in range(len(a)-1):
    for k in range(len(a)-1):
        if a[k]>a[k+1]:
            a[k],a[k+1]=a[k+1],a[k]
        print(a[k],end=' ')
    print()
print()
for m in range(len(a)):
    for n in range(len(a)):
        if a[m]==b[n]:
            index=n
    print(f'{a[m]} is at position {index}')