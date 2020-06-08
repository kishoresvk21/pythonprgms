n=input()
res=''
l=[]
for i in range(len(n)):
    if(n[i].isalnum()):
        res+=n[i]
    else:
       l.append(i)
res=res[::-1]
pr=''
count=0
for i in range(len(n)):
    if i in l:
        pr+=n[i]
    else:
        pr+=res[count]
        count+=1
print(pr)
        
'''
1)
special  string reverse
 Input Format:
 	b@rd
 output Format:
	d@rb
 Explanation:
	We should reverse the alphabets of  the  string by keeping the special characters in  the  same  position
	'''
