class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        mylist=[]
        mylist.append(nums[0])
        
        for i in range(1,len(nums)):
            
            mylist.append(nums[i])
            mylist[-1] = mylist[-1]+mylist[-2]
        
        return(mylist)
        
#         total=0
#         mylist=[]
        
#         for num in nums:
#             total+=num
            
#             mylist.append(total)
            
#         return(mylist)