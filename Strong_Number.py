def fact(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
n=int(input())
s=0
z=n
while n:
    a=n%10
    s=s+fact(a)
    n=n//10
if z==s:
    print('The number',z,'is a strong number')
else:
    print('The number',z,'is not a strong number')