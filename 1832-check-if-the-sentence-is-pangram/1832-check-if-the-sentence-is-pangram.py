class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return
        table={}
        for i in range(97,123,1):
            table[i]=1
        
        for letter in sentence:
            if ord(letter) in table:
                del table[ord(letter)]
                
        if not table:
            return True
        return