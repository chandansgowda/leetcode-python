class Solution:
    def countPoints(self, rings: str) -> int:
      rods = [set() for _ in range(10)]
      i = 0
      ans = 0
      alreadyCounted = set()
      while i<len(rings):
        color = rings[i]
        pos = int(rings[i+1])
        rods[pos].add(color)
        i+=2
      for s in rods:
        if len(s)==3:
          ans+=1
      return ans

        
