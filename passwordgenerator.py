passw=''
for i in input().split(','):
    s,n=i.split(':')
    if(str(len(s)) in n):
        passw+=s[-1]
        continue
    temp=int(min(n))
    flag=0
    for i in n:
        if(int(i)<=len(s) and int(i)>=temp):
            flag=1
            temp=int(i)
    if(flag==0):
        passw+='X'
    else:
        passw+=s[temp-1]
print(passw)
'''

Given input of array of string in format <emp name> <emp number> separated by comas , 
Emp should contain only alphabets and employee number. 

You have to generate password for 
Ex : input Robert:36787,Tina:68721,Jo:56389   
Output :tiX   
Conditions: len of robert is 6 and 6 is present in emp number robert (36787),so return the alphabet at position 6 that is t.   

Now len of tina is 4 and 3 is not present in the 68721 so select the number which is max and less than the len of tina so select 2 return the alphabet that is at position 2 that is i. 

Now ln of Jo is 2 it is not present in 56389 and there is not present any number which is less than 2 so return X.
'''
