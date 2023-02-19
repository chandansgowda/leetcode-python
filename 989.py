class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num)-1
        num[i] += k

        while i>0:
            if num[i]>9:
                c,num[i] = divmod(num[i],10)
                num[i-1]+=c
            i-=1

        while num[i]>9:
            c,num[i] = divmod(num[i],10)
            num.insert(0,c)
            

        return num
