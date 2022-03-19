class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        str1=''
        mylist=[]
        
        if len(s)==0 or len(s)==1:
            return len(s)

        else:
            for i in range(len(s)):
                str1=''
                str1+=s[i]
                for j in range(i+1,len(s)):
                    if s[j] not in str1:
                        str1+=s[j]
                        if j==len(s)-1:
                            mylist.append(len(str1))
                        # print(str1)
                    else:
                        if len(str1) not in mylist:
                            mylist.append(len(str1))
                        break

            return(max(mylist))
        

            
        