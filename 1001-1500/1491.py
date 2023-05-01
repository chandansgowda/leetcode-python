class Solution:
    def average(self, salary: List[int]) -> float:
        s = sum(salary) - max(salary) - min(salary)
        return s/(len(salary)-2)
