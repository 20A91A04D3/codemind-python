n=int(input())
s=0
while n:
    a=n%10
    s=s+(a**2)
    n=n//10
    if s>9 and n==0:
        n=s
        s=0
if s==1 or s==7:
    print('True')
else:
    print('False')