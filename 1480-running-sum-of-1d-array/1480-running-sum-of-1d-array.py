class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        total=0
        mylist=[]
        
        for num in nums:
            total+=num
            
            mylist.append(total)
            
        return(mylist)