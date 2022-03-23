class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s)!=len(goal):
            return
        
        
        s=list(s)
        nl=[]
        
        for k in range(len(s)):
            temp=None
            last=s[len(s)-1]
            for i in range(len(s)-1):

                if temp==None:
                    temp=s[i+1]
                    s[i+1]=s[i]
                else:
                    temp2=s[i+1]
                    s[i+1]=temp
                    temp=temp2
            s[0]=last
            print(s)
            # nl.append(s)
            goal=list(goal)
            if goal==s:
                return True
        return
        
        # goal=list(goal)
        # print(goal)
        # if goal in nl:
        #     return True
        # return False
                