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
    for j in range(i+1,len(l)+1):
        count=l.count(1)
        for k in l[i:j]:
            if(k==0):
                count+=1
            else:
                count-=1
        if(count>ma):
            ma=count
print(ma)



#2nd type
'''
n = int(input()) # Number of elements in the array 

arr = list(map(int, input().split())) # Array containing 0s and 1s 

ones_count = [] 

# Use two for loops to creat subarrays 
for i in range(n): 
	for j in range(i + 1, n + 1): 
		
		# arr[i:j] is a subarray 
		# The main logic to calculate count of 1s 
		ones_count.append(arr.count(1)+arr[i:j].count(0)-arr[i:j].count(1)) 
		
# finally, maximum of ones_count will be the required answer	 
print(max(ones_count)) 
'''
