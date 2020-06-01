n=input().split(' ')
sum=0
flag=0
for i in range(len(n)-1):
    sum+=int(n[i])
    if(n[i].startswith('0')):
        flag=1
if(sum==int(n[-1]) and flag==0):
    print("Valid")
else:
    print("Invalid")
