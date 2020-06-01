d={}
res=[]
for i in range(int(input())):
    s=''
    l=input().split()
    if(l[0]=='add'):
        for i in l[1]:
            s=s+i
            if(s not in d):
                d[s]=1
            else:
                d[s]+=1
    else:
        if(l[1] in d):
            res.append(d[l[1]])
        else:
            res.append(0)
for i in res:
    print(i)
            
