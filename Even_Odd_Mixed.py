n=int(input())
l=len(str(n))
o=0
e=0
while n:
    a=n%10
    if a%2==0:
        e+=1
    else:
        o+=1
    n=n//10
if e==l:
    print('Even')
elif o==l:
    print('Odd')
else:
    print('Mixed')