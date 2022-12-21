class Node:
    def __init__(self, val=None, nextP=None, prev=None):
        self.val = val
        self.next = nextP
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Node(homepage)
        self.curr = self.history
        

    def visit(self, url: str) -> None:
        newUrl = Node(url)
        newUrl.prev = self.curr
        self.curr.next = newUrl
        self.curr = newUrl
        

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)