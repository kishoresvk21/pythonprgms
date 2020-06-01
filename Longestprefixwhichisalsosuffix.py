'''
Given a string s, find length of the longest prefix which is also suffix. The prefix and suffix should not overlap.

Examples:

Input : aabcdaabc
Output : 4
The string "aabc" is the longest
prefix which is also suffix.

Input : abcab
Output : 2

Input : aaaa
Output : 2
'''

n=input()
res=''
i=0
while(True):
    if(n[:i+1]==n[-(i+1):]):
        res=n[:i+1]
        print(res)
    if(i==len(n)//2-1):
        break
    i+=1
print(len(res))
        
    
'''
#2nd method of same
# Python3 program to find length 
# of the longest prefix which 
# is also suffix 

def longestPrefixSuffix(s) : 
	n = len(s) 
	
	for res in range(n // 2, 0, -1) : 
		
		# Check for shorter lengths 
		# of first half. 
		prefix = s[0: res] 
		suffix = s[n - res: n] 
		
		if (prefix == suffix) : 
			return res 
			

	# if no prefix and suffix match 
	# occurs 
	return 0
	
s = "blablabla"
print(longestPrefixSuffix(s)) 

# This code is contributed by Nikita Tiwari. 
