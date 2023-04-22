class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curPage = 0
        

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curPage+1] + [url]
        self.curPage += 1

    def back(self, steps: int) -> str:
        self.curPage = max(0,self.curPage-steps)
        return self.history[self.curPage]

    def forward(self, steps: int) -> str:
        self.curPage = min(len(self.history)-1,self.curPage+steps)
        return self.history[self.curPage]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
