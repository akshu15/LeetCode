class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        
        # print(boxTypes)
        total = 0
        size = truckSize
        for i in range(len(boxTypes)):
            
            if size - boxTypes[i][0] > 0:
                total = total + ((boxTypes[i][1]) * boxTypes[i][0])
            else:
                total = total + ((boxTypes[i][1]) * abs(size)) 
                break
            size = size - boxTypes[i][0]
        return(total)