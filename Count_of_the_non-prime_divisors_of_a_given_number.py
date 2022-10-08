def prime(n):
    for i in range(2,n):
        if n%i==0:
            return True
    return False
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i)==True:
            c+=1
print(c+1)
