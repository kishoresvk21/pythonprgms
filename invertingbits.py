'''
You are given an array of size n. Each element in the array is either 0 or 1. You have to perform exactly one operation. In one operation you need to select a subarray and invert all the bits in the subarray. The minimum size of the subarray to be selected is 1 and the maximum size is n.

Print the maximum number of 1s that you can get by doing the operation described above.

[Note: Inversion means changing a 0 to 1 and a 1 to 0]

 

Test Case:

Input:
6
1 0 0 1 0 1
Output:
5
'''
n=int(input())
l=list(map(int,input().split()))
ma=0
for i in range(len(l)):
    for j in range(i,len(l)+1):
        count=l.count(1)
        for k in l[i:j]:
            if(k==0):
                count+=1
            else:
                count-=1
        if(count>ma):
            ma=count
print(ma)
