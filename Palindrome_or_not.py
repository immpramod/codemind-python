s=input()
t=s.lower()
rev=''
for ch in t:
    rev=ch+rev
for i in range(len(t)):
    if(rev[i]==t[i]):
         print('True')
         break;
    else:
         print('False')
         break;