class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashMap = {}
        
        for i in range(len(nums2)):
            
            if i == len(nums2)-1:
                hashMap[nums2[i]]=-1
                
            for j in range(i+1, len(nums2)):
                if nums2[i] not in hashMap:
                    if nums2[i] < nums2[j]:
                        hashMap[nums2[i]] = nums2[j]
                        break
                    if j == len(nums2)-1:
                        hashMap[nums2[i]]=-1
        # print(hashMap)
        
        output=[]
        
        for num in nums1:
            output.append(hashMap[num])
        return(output)
                    
                    
                
                