from random import*
type=randint(0,3)
numb=randint(1,13)
from random import*
type1=randint(0,3)
numb1=randint(1,13)
from random import*
type2=randint(0,3)
numb2=randint(1,13)
if type==0:
    type = 'C'
elif type==1:
    type = 'S'
elif type==2:
    type = 'D'
elif type==3:
    type = 'H'
if numb==1:
    numb='Ace'
if numb==2:
    numb='Two'
if numb==3:
    numb='Three'
if numb==4:
    numb='Four'
if numb==5:
    numb='Five'
if numb==6:
    numb='Six'
if numb==7:
    numb='Seven'
if numb==8:
    numb='Eight'
if numb==9:
    numb='Nine'
if numb==10:
    numb='Ten'
if numb==11:
    numb='Jack'
if numb==12:
    numb='King'
if numb==13:
    numb='Queen'
print(f"Card 1 is a {numb} of {type}.")
print(f"Card 2 is a {numb} of {type}.")
print(f"Card 3 is a {numb} of {type}.")
