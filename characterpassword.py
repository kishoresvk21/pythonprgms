s=list(input())
l=[]
for i in s:
    temp1=ord(i)-96+ord(i)
    temp2=temp1%26
    temp3=chr(temp2+96)

    l.append(temp3)
print("".join(l))
