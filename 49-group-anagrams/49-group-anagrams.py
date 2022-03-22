class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap={}
        
        # nList=[]
        if len(strs)>=1:
            
            for i in range(len(strs)):


                my=list(strs[i])
                my.sort()
                # print(my)
                if tuple(my) in hashMap:
                    hashMap[tuple(my)].append(strs[i])
                else:
                    hashMap[tuple(my)]=[strs[i]]

                # for i in range(hashMap[i])

            return(hashMap.values())
        else:
            return