class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        str1=s.split(" ")
        # print(str1)
        for i in range(len(str1)-1,-1,-1):
            if str1[i].isalpha():
                return(len(str1[i]))
            
        
    