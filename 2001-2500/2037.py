class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        x = 0
        for i in range(len(seats)):
            x += abs(seats[i]-students[i])
        return x
