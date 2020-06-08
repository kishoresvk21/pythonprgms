n=input()
l=set()
e=set()
for i in n:
    if(i.isdigit() and i not in l):
        l.add(int(i))
        if(int(i)%2==0):
            e.add(int(i))
l=sorted(l,reverse=True)
if(len(e)==0):
    print(-1)
else:
    l.remove(min(e))
    res=''
    for i in l:
        res+=str(i)
    res+=str(min(e))
    print(res)
'''
A string which is a mixture of letter and integer and special char from which find the largest even number from the available digit after removing the duplicates.   

If an even number is not formed then return -1.   

Ex : infosys@337 
O/p : -1   

Hello#81@21349 
O/p :983412
'''
