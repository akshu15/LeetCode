class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        print(nums)
        
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)

                