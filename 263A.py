for i in range(0, 5):
    row=input().split()
    for j in range(0, 5):
        if row[j] == '1':
            print(abs(2-i)+abs(2-j))
            break
        
