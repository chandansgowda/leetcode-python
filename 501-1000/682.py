class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for i in operations:
            if i=="C":
                l.pop()
            elif i=="D":
                l.append(l[-1]*2)
            elif i=="+":
                l.append(l[-1]+l[-2])
            else:
                l.append(int(i))
        print(l)
        return sum(l)
