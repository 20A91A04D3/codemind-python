n=int(input())
p=0
s=0
while n:
    a=n%10
    s=s+(a*8**p)
    p+=1
    n=n//10
print(bin(s)[2:])