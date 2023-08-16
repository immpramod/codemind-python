s=list(input().split())
mn,mx=0,0
x=0
for i in s:
    mn=ord(min(i))
    mx=ord(max(i))
    x=x+(mx-mn)
print(x)