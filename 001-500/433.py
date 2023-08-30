class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque()
        q.append((startGene,0))
        visited = {startGene}
        while q:
            node, steps = q.popleft()
            if node==endGene:
                return steps
            for c in 'ATGC':
                for i in range(len(node)):
                    x = node[:i] + c + node[i+1:]
                    if x not in visited and x in bank:
                        q.append((x,steps+1))
                        visited.add(x)
        
        return -1
