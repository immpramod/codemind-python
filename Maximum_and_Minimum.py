n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if i not in c and l.count(i)==i:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    print(min(c),max(c))