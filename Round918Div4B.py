iterations=int(input())
solution=[]
for i in range(0, iterations):
    possible=['A', 'B', 'C', '?']
    for k in range(0, 3):
        possible=['A', 'B', 'C', '?']
        r1=[]
        uu=input()
        for l in range(0, len(uu)):
            r1.append(uu[l])
        if '?' in r1:
            for j in r1:
                possible.remove(j)
            solution.append(possible[0])
for i in solution:
    print(i)