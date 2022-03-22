class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap={}
        
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]]+=1
            else:
                hashMap[nums[i]]=1
                
        # max_keys = [key for key, value in hashMap.items() if value == max(hashMap.values())]
        
        # print(max_keys)
        
        mylist=[]
        
        for i in range(k):
            max_key = max(hashMap,key=hashMap.get)
            mylist.append(max_key)
            hashMap.pop(max_key)
            
        return(mylist)
            
            