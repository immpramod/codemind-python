def rev(n):
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n=n//10
    return s
    
n=int(input())
while(n):
    n+=rev(n)
    if (rev(n)==n):
        print(n)
        break
else:
    print('-1')
