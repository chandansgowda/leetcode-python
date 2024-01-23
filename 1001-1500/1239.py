class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(s)==len(set(s))
        def bt(start, cur_s):
            nonlocal max_len
            if is_unique(cur_s):
                max_len = max(max_len, len(cur_s))
            for i in range(start, len(arr)):
                bt(i+1, cur_s+arr[i])
        max_len = 0
        bt(0,"")
        return max_len
