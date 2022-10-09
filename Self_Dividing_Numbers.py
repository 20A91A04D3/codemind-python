def selfdiv(n):
    a=n
    while n:
        x=n%10
        if x!=0:
            if a%x!=0:
                return False
        else:
            return False
        n=n//10
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if selfdiv(i)==True:
        print(i,end=' ')