char=input('Character :')
order=ord(char)
if order&1==0:
    order=order|1
else:
    order=order&~1
if order&2==0:
    order=order|2
else:
    order=order&~2
if order&4==0:
    order=order|4
else:
    order=order&~4
if order&8==0:
    order=order|8
else:
    order=order&~8
if order&16==0:
    order=order|16
else:
    order=order&~16
if order&32==0:
    order=order|32
else:
    order=order&~32
print(f'Charachter after flip : {chr(order)} ')