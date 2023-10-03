i=1
x=1
while i<100:
    if x<10:
        print(f'[{x}]')
    if x>=10:
        left=x//10
        right=x%10
        add=left+right
        print(f'[{x} {add}]')
        if add>=10:
            left1=add//10
            right1=add%10
            add1=left1+right1
            print(f'[{x} {add} {add1}]')
    i=i+1
    x=x+1