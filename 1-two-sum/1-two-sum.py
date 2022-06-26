class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashT = {}
        
        for i in range(len(nums)):
            newTarget = target  - nums[i] 
            
            if newTarget not in hashT:
                hashT[nums[i]] = i
            else:
                return (hashT[newTarget], i)