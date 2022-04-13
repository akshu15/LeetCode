class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        # print(nums)
        nums1=list(set(nums))
        nums1.sort() 
        # print(nums1)
        if nums1==nums:
            # print("ji")
            return False
        
        return True
        