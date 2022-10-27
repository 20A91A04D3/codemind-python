for _ in range(int(input())):
    a=int(input())
    l=len(str(a))
    s=0
    p=0
    while a:
        k=a%10
        s=s+(k*2**p)
        p+=1
        a=a//10
    print(oct(s)[2:])
        