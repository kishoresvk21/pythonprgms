a=input()
i=0
def repeat(j,str1):
    val=''
    while(not a[j].isalpha()):
        val+=a[j]
        j+=1
    temp=int(val)
    print(str1*temp,end='')
for i in range(0,len(a)):
    if(a[i].isalpha() and i<len(a)):
        repeat(i+1,a[i])
