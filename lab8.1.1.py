i=1
count=0
rows=int(input('Rows : '))
while i<=1:
    char=65
    while char<=84:
     print(chr(char),end=' ')
     count=count+1
     if count%4==0:
        print()
     char=char+1
    i=i+1