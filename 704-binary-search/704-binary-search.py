class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        def newSearch(nums, left, right, target):
            mid = (left + right)//2
            
            if(left>right): 
                return -1
            
            if(nums[mid]==target):
                return mid
            
            elif(target<nums[mid]):
                right=mid-1
                return newSearch(nums, left, right, target)
                
            elif(target>nums[mid]):
                left=mid+1
                return newSearch(nums, left, right, target)
            
        
        mid = newSearch(nums, left, right, target)
        return mid
                