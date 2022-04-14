class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if nums==[]:
            return [-1,-1]
        
        left,right=0,len(nums)-1

        l=[]
        
        while left<=right:
            
            if nums[left]==target:
                l.append(left)
            if nums[right]==target:
                l.append(right)
            left+=1
            right-=1
        if l==[]:
            return [-1,-1]
        l.sort()

        return([l[0],l[-1]])