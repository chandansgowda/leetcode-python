class Solution:
    def candy(self, ratings: List[int]) -> int:
        rtl = [1]*len(ratings)
        ltr = [1]*len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i-1]<ratings[i]:
                ltr[i] = ltr[i-1]+1

        for i in reversed(range(len(ratings)-1)):
            if ratings[i+1]<ratings[i]:
                rtl[i] = rtl[i+1]+1

        ans = 0
        for i in range(len(ratings)):
            ans += max(ltr[i],rtl[i])

        return ans
