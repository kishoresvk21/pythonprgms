n=input()
flag=0
for i in range(len(n)):
    res=''
    for i in n[i:]:
        if(i.lower() in res.lower()):
            break
        else:
            res+=i
    if(len(res)>3):
        print(res)
        flag=1
        break
if(flag==0):
    print(-1)
'''
2)  
A string is given we have to find the longest substring which is unique (that has no repetition ) and min size is 3. 
 
 If more than one sub string is found with max length the we have to print one which appered first in thw string If no substring is present which matches the condition then we have to print -1; 
Ex :input : “A@bcd1abx” 
Output : “A@bcd1”
'''
