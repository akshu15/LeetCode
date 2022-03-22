class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        hashMap={}
        
        # key_list=[]
        val_list=[]
        
        for i in range(len(nums)):
            hashMap[i]=nums[i]
            # key_list.append(i)
            val_list.append(hashMap[i])
            
        # print(hashMap)
        return(val_list[len(nums)-k])
        
        
        
        
        
            
            
            