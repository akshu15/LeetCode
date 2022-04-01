class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #in ["flower","flow","floor","flight"] 
        #max->"flower" 
        #Reason: till 'fl' everyword is on same level
        #at 3rd char we have 3 words ["flower", "flow" and "floor"]
        #then on proceeding to the next 4th character of every word
        #we get ["flower", "flow"] whose "w" is alphabetically greater than floor's : "o"
        #atlast we get flower
        #min->"flight"
        #since at 3rd char flight's "i" is alphabetically less than every word's
        
        
        maxStr=max(strs) 
        minStr=min(strs)
        
        for i, ch in enumerate(minStr):
            
            if ch==maxStr[i]:
                continue
            else:
                return minStr[:i]
            
        return minStr
        