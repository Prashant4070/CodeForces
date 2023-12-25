code=input()
soln=''
i=0
while i<len(code):
    if code[i]=='.':
        soln+='0'
        i+=1
    elif code[i]=='-' and code[i+1]=='.':
        soln+='1'
        i+=2
    elif code[i]=='-' and code[i+1]=='-':
        soln+='2'
        i+=2
print(soln)