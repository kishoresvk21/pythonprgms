def anagram(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    count=0
    if(len(str1)==len(str2)):
        for i in str1:
            if i in str2:
                count+=1
    if(len(str1)==count):
        print("Anagram")
    else:
        print("Not anagram")
anagram("Listen","Silent")
anagram("modern","norman")

        
