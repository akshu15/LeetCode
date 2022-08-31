class Solution:
    def myAtoi(self, s: str) -> int:
        
        s=s.lstrip() ##stripping off spaces from the start Eg: "  42 "=> "42 " 
        
       
        str1=''
        flag=False
        if s=="":
            return 0
        
        elif (s[0].isalpha() or s[0]=='.'):
            return 0
        
        elif len(s)==1:
            if s=="+" or s=="-":
                return 0
            else:
                return s
            
        else:
            for char in range(len(s)):

                if s[char].isalpha() or s[char]==' ' or s[char]=='.':
                    if char!=0 and (s[char-1]=='+' or s[char-1]=='-'):
                        return 0
                    break

                elif (s[char]=='+' or s[char]=='-'):
                    if(char==0):
                        str1=str1+s[char]
                    elif(s[char-1]=='+' or s[char-1]=='-'):
                        return 0
                    else:
                        break

                else:
                    str1=str1+s[char]

            str2=int(str1)
            if str2 > (2**31)-1:
                return((2**31)-1)
            elif str2< -(2**31):
                return(-(2**31))

            else:
                return(str2)
        
            
            
            
                
                