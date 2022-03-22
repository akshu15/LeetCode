class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hashMap={}
        myList=[]
        el=[]
        
        for i in range(len(numbers)):
            
            if target - numbers[i] in hashMap:
                
                a=hashMap[target - numbers[i]]+1
                b=i+1
                myList+=[a]+[b]
                # myList.append(el)
                return(myList)
            
            else:
                hashMap[numbers[i]]=i
        