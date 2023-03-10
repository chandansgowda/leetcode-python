class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                count += set(words[i]) == set(words[j])

        return count
