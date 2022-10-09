a=int(input())
b=int(input())
d1=0
d2=0
for i in range(1,a):
    if a%i==0:
        d1+=i
for j in range(1,b):
    if b%j==0:
        d2+=j
if d1==b and d2==a:
    print('Amicable')
else:
    print('Not Amicable')