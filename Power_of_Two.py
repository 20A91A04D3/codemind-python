n=int(input())
k=0
s=0
while n:
    s=2**k
    if s==n:
        print('True')
        break
    elif s>n:
        print('False')
        break
    else:
        k+=1