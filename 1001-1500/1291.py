class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        x = "123456789"
        ans = []

        for i in range(len(x)):
            for j in range(i + 1, len(x) + 1):
                curr = int(x[i:j])
                if low <= curr <= high:
                    ans.append(curr)
        return sorted(ans)
