class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()

        nums1=list(set(nums))
        nums1.sort() 

        if nums1==nums:
            return False
        
        return True
        