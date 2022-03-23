class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        if intervals==None:
            return
        elif len(intervals)==1:
            return intervals
        else:
            
            start=intervals[0][0]
            end=intervals[0][1]
            
            mylist=[]
            
            for i in range(1,len(intervals)):
                
                if intervals[i][0]<=end:
                    end=max(intervals[i][1],end)
                    
                else:
                    
                    s=[]
                    s+=[start]+[end]
                    
                    mylist.append(s)
                    
                    start=intervals[i][0]
                    end=intervals[i][1]
                    
            if intervals[len(intervals)-1][0]<=end:
                end=max(intervals[len(intervals)-1][1],end)
            
                s=[]
                s+=[start]+[end]
                    
                mylist.append(s)
            
            return(mylist)
                    
                    
                    
                    