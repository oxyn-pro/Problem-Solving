class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur_page_idx = 0
        self.history_length = 1
        self.history = [homepage]

    # TC: O(1)
    # SC: O(1)
    def visit(self, url: str) -> None:
        if self.cur_page_idx < len(self.history) - 1:
            self.history[self.cur_page_idx + 1] = url
        else:
            self.history.append(url)

        self.cur_page_idx += 1
        self.history_length = self.cur_page_idx + 1

    # TC: O(1)
    # SC: O(1)
    def back(self, steps: int) -> str:
        self.cur_page_idx = max(self.cur_page_idx - steps, 0)
        return self.history[self.cur_page_idx]

    # TC: O(1)
    # SC: O(1)
    def forward(self, steps: int) -> str:
        self.cur_page_idx = min(self.cur_page_idx + steps, self.history_length - 1)
        return self.history[self.cur_page_idx]


br = BrowserHistory("leetcode")
br.visit("google")
br.visit("facebook")
br.visit("youtube")
br.back(1)
br.back(1)
br.forward(1)
br.visit("leetcode")
br.forward(2)
br.back(7)
