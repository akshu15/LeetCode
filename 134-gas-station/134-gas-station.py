class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start_gas = 0
        index = 0
        for i in range(len(gas)):
            start = gas[i] - cost[i]
            
            if tank + start < 0:
                tank = 0
                index = i + 1
            else:
                tank += start
                
            start_gas += start
        
        return index if start_gas >= 0 else -1