i=1
x=1
while i<=100:
    if x>=1 and x<10:
      if x==1:
        print('One')
      if x==2:
        print('Two')
      if x == 3:
        print('Three')
      if x == 4:
        print('Four')
      if x == 5:
        print('Five')
      if x == 6:
        print('Six')
      if x == 7:
        print('Seven')
      if x == 8:
        print('Eight')
      if x == 9:
        print('Nine')
    if x>=10 and x<20:
        if x==10:
            print('Ten')
        if x==11:
            print('Eleven')
        if x==12:
            print('Twelve')
        if x==13:
            print('Thirteen')
        if x==14:
            print('Fourteen')
        if x==15:
            print('Fifteen')
        if x==16:
            print('Sixteen')
        if x==17:
            print('Seventeen')
        if x==18:
            print('Eighteen')
        if x==19:
            print('Nineteen')
    if x>=20:
        left=x//10
        right=x%10
        if left==2:
            left='Twenty'
        elif left==3:
            left='Thirty'
        elif left==4:
            left='Forty'
        elif left==5:
            left='Fifty'
        elif left==6:
            left='Sixty'
        elif left==7:
            left='Seventy'
        elif left==8:
            left='Eighty'
        elif left==9:
            left='Ninety'
        if right==0:
            right=''
        elif right==1:
            right='One'
        elif right==2:
            right='Two'
        elif right==3:
            right='Three'
        elif right==4:
            right='Four'
        elif right==5:
            right='Five'
        elif right==6:
            right='Six'
        elif right==7:
            right='Seven'
        elif right==8:
            right='Eight'
        elif right==9:
            right='Nine'
        print(f'{left} {right}')
    if x==100:
        print('Hundred')
    i=i+1
    x=x+1







