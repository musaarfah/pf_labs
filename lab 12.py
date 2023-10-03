from random import*
LENGTH = randint(5,9)
d = [[randint(1,9) for i in range(LENGTH)] for j in range(LENGTH)]
for i in range(LENGTH):
    d[i][i]=0
print(d)
for i in range(LENGTH):
    for j in range(LENGTH):
        print(d[i][j],end=' ')
    print()
print()


def find_directdist(a,b,c):
        print(f'Direct Distance : {d[b][c]}')
        for i in range(LENGTH):
            if i!=b and i!=c:
              print(f'via city {i} : {d[b][i]+d[i][c]}')

find_directdist(d,1,2)

def find_shortest_distance(a, b, c):
    minim=0
    if minim<d[b][c]:
        minim=d[b][c]
    for i in range(LENGTH):
        if i != b and i != c:
            indirect=d[b][i] + d[i][c]
            if indirect<minim:
                minim=indirect
    print(f'Shortest Distance between city {b} and city {c} is {minim}')

find_shortest_distance(d,1,2)

def shortest(d):
    min = 100
    for i in range(LENGTH):
        for j in range(LENGTH):
            if i != j:
                if d[i][j] < min:
                    min = d[i][j]
                    city1 = i
                    city2 = j
    print(f'city {city1} and city {city2} has shortest direct distance{min}')
shortest(d)

