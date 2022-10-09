l=int(input())
for _ in range(int(input())):
    w,h=map(int,input().split())
    ma=max(w,h)
    mi=min(w,h)
    if ma<l or mi<l:
        print('UPLOAD ANOTHER')
    elif ma==mi==l:
        print('ACCEPTED')
    elif ma>l or mi>l:
        if ma==mi:
            print('ACCEPTED')
        else:
            print('CROP IT')