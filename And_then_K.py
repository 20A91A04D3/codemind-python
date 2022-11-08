for _ in range(int(input())):
    n=int(input())
    p=0
    s=0
    while n:
        s=s+2**p
        if n-2**p<2**p:
            print(s-2**p)
            break
        p+=1
        