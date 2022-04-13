class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap={}
        
        for num in nums:
            if num in hashMap:
                hashMap[num]+=1
            else:
                hashMap[num]=1
                
        for key, val in hashMap.items():
            if val==1:
                return key
            
        