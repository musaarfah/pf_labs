from random import*
i=1
while i<=10:
    num1=randint(1,9)
    num2=randint(1,9)
    print(f'Number 1 = {num1}  Number 2 ={num2}')
    sum=int(input('Sum : '))
    difference=int(input('Difference : '))
    product=int(input('Product : '))
    if sum==(num1+num2):
        marks=1
    if sum!= (num1+num2):
        marks=0
        print('Wrong Sum')
        sum1=int(input('Enter again : '))
        if sum1==(num1+num2):
            marks=1
        if sum1!=(num1+num2):
            marks =0
            print('wrong sum')
        sum2=int(input('Enter Again:'))
        if sum2==(num1+num2):
            marks=1
    if product==(num1*num2):
        marks=1
    if product!= (num1*num2):
        marks=0
        print('Wrong Product')
        product1=int(input('Enter again : '))
        if product1==(num1*num2):
            marks=1
        if product1!=(num1*num2):
            marks =0
            print('wrong Product')
        product2=int(input('Enter Again:'))
        if product2==(num1*num2):
            marks=1
    i=i+1

