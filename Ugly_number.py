def prime(n):
    for i in range(2,n):
        if n%i==0:
            if i%2!=0 or i%3!=0 or i%5!=0:
                return False
    return True
n=int(input())
if n==1:
    print('Ugly Number')
else:
    if prime(n)==True:
        print('Not Ugly Number')
    else:
        print('Ugly Number')