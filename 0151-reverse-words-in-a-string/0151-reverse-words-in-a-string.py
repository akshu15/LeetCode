class Solution:
    def reverseWords(self, s: str) -> str:
        
        s=s.split(' ')
        s=s[::-1]
        newS = ''
        for i in s:
            if i =='':
                continue
            else:
                newS = newS + ' '+i
        return(newS.lstrip())