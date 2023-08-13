n=int(input())
l=list(map(int,input().split()))
o=[]
e=[]
for i in range(n):
    if l[i]%2==0:
        e.append(l[i])
    if l[i]%2!=0:
        o.append(l[i])
i=0
j=0
while i<len(e) or j<len(o):
    if i<len(e):
        print(e[i],end=' ')
        i+=1
    if j<len(o):
        print(o[j],end=' ')
        j+=1
if n%2!=0:
    print(0)