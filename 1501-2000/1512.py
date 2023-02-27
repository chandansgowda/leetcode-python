# Hashmap Approach
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memory = {}
        count = 0

        for num in nums:
            if num in memory:
                if memory[num]==1:
                    count+=1
                else:
                    count+=memory[num]
                memory[num]+=1
            else:
                memory[num]=1

        return count



# Bruteforce approach
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1

        return count
