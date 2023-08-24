n=int(input())
while(n):
    n-=1
    a=int(input())
    l=list(map(int,input().split()))[:a]
    if sorted(l)==l:
        print('0')
    else:
        print(max(l)-min(l))