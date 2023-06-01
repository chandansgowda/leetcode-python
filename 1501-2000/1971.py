class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(graph,node):
            stack = [node]
            visited = set()
            while stack:
                node = stack.pop()
                if node==destination:
                    return True
                if node not in visited:
                    visited.add(node)
                    for child in graph[node]:
                        if child not in visited:
                            stack.append(child)
            return False

        graph = defaultdict(list)

        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)

        return dfs(graph,source)


        
