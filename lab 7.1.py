from random import*
i=1
count=0
while i<=10:
    num1=randint(0,99)
    num2=randint(0,99)
    num3=randint(10,99)
    num4=num3+randint(0,99)
    num5=randint(0,9)
    num6=randint(0,9)
    type=randint(1,3)
    if type == 1:
        print(f'Number 1:{num1} Number 2:{num2} ')
        sum_ans=int(input('Addition Answer:'))
        if sum_ans==(num1 +num2):
            count=count+1
            print('Answer is Correct')
        else:
            count=count+0
            print('Answer is incorrect')
    if type ==2:
        print(f'Number 1:{num4} Number 2:{num3} ')
        sub_ans=int(input('Subtraction Answer :'))
        if sub_ans==(num4-num3):
            count=count+1
            print('Answer is correct')
        else:
            count=count+0
            print('Answer is incorrect')
    if type==3:
        print(f'Number 1:{num5} Number 2:{num6} ')
        mult_ans=int(input('Multiplication Answer : '))
        if mult_ans==num5*num6:
            count=count+1
            print('Answer is correct')
        else:
            count=count+0
            print('Answer is incorrect')
    i=i+1
print(f'Score is {count} out of 10')
