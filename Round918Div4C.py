import math
iterations=int(input())
for i in range(iterations):
    length=int(input())
    numbers=input().split()
    for i in range(0, len(numbers)):
        numbers[i]=int(numbers[i])
    summation=sum(numbers)
    root=math.sqrt(summation)
    root=str(root)
    if(root.split('.')[1])!='0':
        print('No')
    else:
        print('Yes')
