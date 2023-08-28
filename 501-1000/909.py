class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()

        def squarePos(square):
            r = (square-1) // n
            c = (square-1) % n
            if r%2==1:
                c = n-c-1
            return (r,c)

        q = deque()
        q.append((1,0))
        visited = set()
        while q:
            square, moves = q.popleft()
            
            for i in range(1,7):
                nextSquare = square + i
                r,c = squarePos(nextSquare)
                if board[r][c]!=-1:
                    nextSquare = board[r][c]
                if nextSquare==n**2:
                    return moves+1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append((nextSquare, moves+1))
        
        return -1
