m,n=map(int,input().split())
maxnum=max(m,n)
while(True):
    if maxnum%m==0 and maxnum%n==0:
        break
    maxnum=maxnum+1
print(maxnum) 