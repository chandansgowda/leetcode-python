class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n,p,z = [],[],[]
        res = set()

        for num in nums:
            if num==0:
                z.append(num)
            elif num>0:
                p.append(num)
            else:
                n.append(num)

        N,P = set(n), set(p)

        if z:
            for num in P:
                if -num in N:
                    res.add((num,-num,0))

            if len(z)>=3:
                res.add((0,0,0))

        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([target, p[i], p[j]])))

        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([target, n[i], n[j]])))

        return res




class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = nums[i]*-1
            l,r=i+1,len(nums)-1

            while l<r:
                if nums[l]+nums[r]==target:
                    ans.append([nums[l], nums[r], nums[i]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    r-=1

        return ans
