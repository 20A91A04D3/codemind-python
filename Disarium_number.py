n=int(input())
l=len(str(n))
a=n
s=0
while n:
    x=n%10
    s=s+(x**l)
    l-=1
    n=n//10
if s==a:
    print('True')
else:
    print('False')