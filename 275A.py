def switching(switchboard, switches, i, j):
    for k in range(0, switches):
        if i in [0, 1]:
            switchboard[i+1][j]=not(switchboard[i+1][j])
        if i in [1, 2]:
            switchboard[i-1][j]=not(switchboard[i-1][j])
        if j in [0, 1]:
            switchboard[i][j+1]=not(switchboard[i][j+1])
        if j in [1, 2]:
            switchboard[i][j-1]=not(switchboard[i][j-1])
        switchboard[i][j]=not(switchboard[i][j])
switchboard=[[True,True,True], [True,True,True], [True,True,True]]
row1=input().split()
row2=input().split()
row3=input().split()
config=[row1, row2, row3]
for i in range(0, 3):
    for j in range(0, 3):
        switches=int(config[i][j])
        switching(switchboard, switches, i, j)


for i in range(0, 3):
    for k in range(0, 3):
        if switchboard[i][k]==True:
            switchboard[i][k]=1
            print(switchboard[i][k], end='')
        else:
            switchboard[i][k]=0
            print(switchboard[i][k], end='')
    print('\n', end='')

