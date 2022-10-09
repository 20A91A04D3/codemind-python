n=int(input())
a=n*n
s=0
while a:
    x=a%10
    s=s+x
    a=a//10
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')