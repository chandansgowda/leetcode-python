class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter=collections.Counter(nums)
        ans1=ans2=0
        for k,v in counter.items():
            ans1+=v//2
            ans2+=v%2
        return [ans1, ans2]


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = {}
        ans = [0,0]
        for num in nums:
            if num in d:
                d[num]+=1
                if d[num]>1:
                    ans[0]+=d[num]//2
                    d[num]%=2
            else:
                d[num]=1
        for k,v in d.items():
            ans[1]+=v
        return ans
