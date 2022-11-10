class Solution:
    def removeDuplicates(self, s: str) -> str:

        old_s=[s[0]]
        for i in range(1, len(s)):
            if old_s:
                if old_s[-1]==s[i]:
                    old_s.pop()
                else:
                    old_s.append(s[i])
            else:
                old_s.append(s[i])
                
                
        return ''.join(old_s)
                
            