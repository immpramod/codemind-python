t=int(input())
l=list(map(str,input().split()))
s=""
for i in l:s+=(i)
print(eval("0b"+s))