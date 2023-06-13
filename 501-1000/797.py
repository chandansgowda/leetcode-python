class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        stack = [(0,[0])]
        res = []

        while stack:
            node, path = stack.pop()
            if node==n-1:
                res.append(path)
            for child in graph[node]:
                stack.append((child,path+[child]))

        return res
