from random import *
numb= randint(20,99)
left=numb//10
right=numb%10
if left==2:
    left= 'Twenty'
elif left==3:
    left= 'Thirty'
elif left==4:
    left= 'Forty'
elif left==5:
    left= 'Fifty'
elif left==6:
    left= 'Sixty'
elif left==7:
    left= 'Seventy'
elif left==8:
    left= 'Eighty'
elif left==9:
    left= 'Ninety'
if right==0:
    right =''
elif right==2:
    right= 'One'
elif right==3:
     right ='Three'
elif right==4:
    right ='Four'
elif right==5:
    right ='Five'
elif right==6:
    right ='Six'
elif right==7:
    right ='Seven'
elif right==8:
    right ='Eight'
elif right==9:
    right = 'Nine'
print(f"The Number {numb} in English is {left}-{right}.")