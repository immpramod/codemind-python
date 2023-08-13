n = int(input())
l= list(map(int,input().split()))
g=[]
c=0
for i in l:
    if l.count(i)==i and i not in g:
        g.append(i)
        c+=1

print(c)