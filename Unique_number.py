n=int(input())
d=[]
while n:
    a=n%10
    d.append(a)
    n=n//10
b=sorted(list(set(d)))
if len(b)==len(d):
    print('Unique Number')
else:
    print('Not Unique Number')