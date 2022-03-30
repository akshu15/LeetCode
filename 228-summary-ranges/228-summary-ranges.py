class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l=[]
        if len(nums)==0:
            return 
        elif len(nums)==1:
            l.append(str(nums[0]))
            return l
        
        else:
            
            start=nums[0]
            
            str1=''
            for i in range(len(nums)-1):
                
                if i==len(nums)-2:
                    if nums[i]+1==nums[i+1]:
                        end=nums[i+1]
                        str1=str(start)+'->'+str(end)
                        l.append(str1)
                    else:
                        end=nums[i]
                        if start!=end:
                            str1=str(start)+'->'+str(end)
                        else:
                            str1=str(start)
                        l.append(str1)
                        l.append(str(nums[i+1]))
                else:
                
                    if nums[i]+1==nums[i+1]:
                        continue
                    else:
                        end=nums[i]
                        if start!=end:
                            str1=str(start)+'->'+str(end)
                        else:
                            str1=str(start)
                        l.append(str1)
                        start=nums[i+1]
            return(l)
                    