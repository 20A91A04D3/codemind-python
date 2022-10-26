n=int(input())
a=len(str(n))
s=n**2
l=s%pow(10,a)
if l==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')