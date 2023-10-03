from random import *
i=1
roll_no=1
passs=0
fail=0
overall_average=0
average_mid=0
average_sessional=0
average_fianls=0
max_mid=max_sessional=max_fianls=0
min_mid=min_sessional=min_fianls=100
max=0
min=100
print(f'Roll No\t\tMids\tFinals\tSessional\tTotal\tGrade')
while i<=30:
    mid=randint(0,35)
    final=randint(0,40)
    sessional=randint(0,25)
    total=mid+sessional+final
    overall_average=overall_average+total
    average_mid=average_mid+mid
    average_sessional=average_sessional+sessional
    average_fianls=average_fianls+final
    if total>max:
        max=total
    if total<min:
        min=total
    if final>max_fianls:
        max_fianls=final
    if total>=85:
        grade='A'
    elif total>=80:
        grade='A-'
    elif total>=75:
        grade='B'
    elif total>=70:
        grade='B-'
    elif total>=65:
        grade='C'
    elif total>=60:
        grade='C-'
    elif total>=55:
        grade='D'
    elif total>=50:
        grade='D-'
    elif total<50:
        grade='F'
    if total>50:
        passs=passs+1
    if grade=='F':
        fail=fail+1
    print(f'{roll_no}\t\t\t{mid}\t\t{final}\t\t{sessional}\t\t\t{total}\t\t{grade}')
    i=i+1
    roll_no=roll_no+1
overall_average=int(overall_average/total)
average_mid=int(average_mid/30)
average_sessional=int(average_sessional/30)
average_fianls=int(average_fianls/30)
print(f'Pass : {passs}\nFail :{fail}')
print(f'Overall Average : {overall_average}')
print(f'Mid Average : {average_mid}')
print(f'Sessional Average : {average_sessional}')
print(f'Fianls Average : {average_fianls}')
print(f'Maximum Marks : {max}')
print(f'Minimum Marks : {min}')
print(f'Max Marks in finals : {max_fianls}')