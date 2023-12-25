info=input().split()
info[0], info[1]= int(info[0]), int(info[1])
temp=input()
queue=[]
k=0
for i in temp:
    queue.append(i)
for j in range(0, info[1]):
    while (k<(info[0]-1)):
        if queue[k]=='B' and queue[k+1]=='G':
            queue[k]='G'
            queue[k+1]='B'
            k+=2
        else:
            k+=1
    k=0
solution=''
for i in queue:
    solution+=i
print(solution)
        
