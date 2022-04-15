class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap={}
        
        
        #nums[i]=2   second_num=target-nums[i]=9-2=7   is it in hash?
        #No:-    hashMap={ 2: 0 }
        #nums[i]=7. second_num=target-nums[i]=9-7=2   is it in hash?
        #Yes:-   return (i, hashMap[second_num])
        
        
        
        for i in range(len(nums)):
            second_num=target-nums[i]       
            
            if second_num in hashMap:
                return([i,hashMap[second_num]])
            else:
                hashMap[nums[i]] = i 
            
        
        
        
        