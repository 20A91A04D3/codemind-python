def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
for i in range(1,n):
    if n%i==0:
        if prime(i)==True and prime(n//i)==True:
            c+=1
            print(i,n//i)
            break
if c==0:
    print('-1')
    
    