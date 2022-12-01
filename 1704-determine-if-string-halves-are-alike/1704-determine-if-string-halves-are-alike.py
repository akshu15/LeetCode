class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels= {
            'a':1,
            'e':1,
            'i':1,
            'o':1,
            'u':1
        }
            
        acount = 0
        bcount = 0
        for i in range(len(s)//2):
            if s[i].lower() in vowels:
                acount+=1
                
        for i in range(len(s)//2, len(s)):
            if s[i].lower() in vowels:
                bcount+=1
                
        if acount==bcount:
            return True
        return False
        