class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        stack = [0]
        while stack:
            node = stack.pop()
            if node in visited: continue

            visited.add(node)
            if len(visited)==n:
                return True

            for child in rooms[node]:
                if child not in visited:
                    stack.append(child)
        
        return False
