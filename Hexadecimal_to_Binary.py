def hextobin(n):
    return bin(int(n,16))
for _ in range(int(input())):
    n=input()
    a=hextobin(n)[2:]
    if len(a)%4==1:
        print('000'+a)
    elif len(a)%4==2:
        print('00'+a)
    elif len(a)%4==3:
        print('0'+a)
    else:
        print(a)