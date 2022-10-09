n=int(input())
m=1
s=0
while n:
    a=n%10
    s=s+a
    m=m*a
    n=n//10
if m==s:
    print('Spy Number')
else:
    print('Not Spy Number')