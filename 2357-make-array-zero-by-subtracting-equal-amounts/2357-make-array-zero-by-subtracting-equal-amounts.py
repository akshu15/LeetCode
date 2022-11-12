class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        #while stack
        #find min
        #iterate -> subtract min from all, if 0 then pop it
        count = 0
        nums.sort()
        if nums[0]==0:
            i=0
            while i < len(nums) and nums:
                if nums[i]==0:
                    nums.pop(i)
                else:
                    break
        while nums:
            mini = min(nums)
            count+=1
            i=0
            while i < len(nums):
                # print(nums[i] , mini)
                if nums[i] - mini == 0:
                    # print("ji")
                    nums.pop(i)
                else:
                    nums[i] = nums[i] - mini
                    i+=1
                # print(nums)
        return(count)
            