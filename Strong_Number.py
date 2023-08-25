n=int(input())
ss=n
s=0
while(n>0):
    r=n%10
    s1=1
    for i in range(1,r+1):
        s1=s1*i
    s=s+s1
    n=n//10
if(ss==s):
    print("The number",ss,"is a strong number")
else:
    print("The number",ss,"is not a strong number")