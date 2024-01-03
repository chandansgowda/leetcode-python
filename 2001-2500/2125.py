class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr = [row.count("1") for row in bank if "1" in row]
        res = 0
        for i in range(len(arr)-1):
            res+=(arr[i]*arr[i+1])
        return res
        
