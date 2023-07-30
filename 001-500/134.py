class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1

        gas_in_tank = 0
        start = 0
        for i in range(len(gas)):
            gas_in_tank += (gas[i]-cost[i])
            if gas_in_tank<0:
                gas_in_tank = 0
                start = i+1
            
        return start
