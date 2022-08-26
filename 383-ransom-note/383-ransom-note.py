class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap={}
            
        for letter in magazine:
            if letter in hashMap:
                hashMap[letter] += 1
            else:
                hashMap[letter] = 1
        print("magazine",magazine)
        print("ransomNote",ransomNote)
        print(hashMap)
        
        for letter in ransomNote:
            if letter in hashMap:
                if hashMap[letter]>=1:
                    hashMap[letter]-=1
                    print("ff",hashMap)
                else:
                    return False
            else:
                print("l")
                return False
        return True