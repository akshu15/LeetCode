class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        start, end = 0, 1
        
        while end < len(nums):
            
            if nums[start]==nums[end]:
                end+=1
                
            else:
                nums[start+1] = nums[end]
                # nums[end] = nums[start]
                start+=1
                end+=1
                
        return start+1