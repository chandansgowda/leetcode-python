class LUPrefix:

    def __init__(self, n: int):
        self.l = 0
        self.videos = set()

    def upload(self, video: int) -> None:
        self.videos.add(video)
        while self.l+1 in self.videos:
            self.l += 1

    def longest(self) -> int:
        return self.l
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
