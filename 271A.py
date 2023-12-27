i = int(input())
History=[]
i+=1
while i<9999:
    for j in str(i):
        if j in History:
            History=[]
            i+=1
            break
        else:
            History.append(j)
        if len(History)==4:
            print(i)
            break
    if len(History)==4:
        break
    
    
    
