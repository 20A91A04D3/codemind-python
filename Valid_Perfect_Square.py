def sqrt(n):
    a=n**(1/2)
    if a==int(a):
        return True
    return False
for _ in range(int(input())):
    n=int(input())
    print(sqrt(n))