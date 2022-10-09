a,b=map(int,input().split())
n=a//10**b
x=a-(n*10**b)
m=a//10**(len(str(a))-b)
print(max(m,x)-min(m,x))