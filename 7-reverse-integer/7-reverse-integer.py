class Solution:
    def reverse(self, x: int) -> int:
        
        if x==0:
            return 0
        str1=str(x)
        # print(str1[0])
        
        if str1.isnumeric():
            str1=str1.rstrip('0')
            rev=str1[::-1]
            
        else:
            sign=str1[0]
            str1=str1.rstrip('0')
            str1=str1[1::]
            rev=sign+str1[::-1]
        
        if int(rev)<(-2**31) or int(rev) > ((2**31)-1):
            return 0
        else:
            return rev
        