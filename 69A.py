number=int(input())
forces=[]
netx=0
nety=0
netz=0
for i in range(0, number):
    f=input().split()
    forces.append(f)
for i in range(0, len(forces)):
    netx+=int(forces[i][0])
    nety+=int(forces[i][1])
    netz+=int(forces[i][2])
if netx==nety==netz==0:
    print("YES")
else:
    print("NO")
