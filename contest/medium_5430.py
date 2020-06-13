
# https://leetcode-cn.com/contest/weekly-contest-192/problems/design-browser-history/

class BrowserHistory:

  def __init__(self, homepage: str):

    self.url_str = [homepage]
    self.future = []
    self.idx = 0

  def visit(self, url: str) -> None:
    if self.future:
      self.url_str = self.url_str[0:self.idx+1]
    self.url_str.append(url)
    self.future = []
    self.idx = len(self.url_str)-1
    # return self.url_str[self.idx]

  def back(self, steps: int) -> str:
    if steps > self.idx:
      self.future = self.url_str[1:]
      self.idx = 0
      return self.url_str[self.idx]
    else:

      self.future = self.url_str[self.idx-steps+1:]
      self.idx = self.idx-steps

      #return self.url_str[len(self.url_str)-1-steps]
      return self.url_str[self.idx]


  def forward(self, steps: int) -> str:
    if not self.future: return self.url_str[self.idx]
    if steps > len(self.future):
      self.idx = self.idx + len(self.future)
      ans = self.future[-1]
      self.future = []
      return ans
    if steps <= len(self.future):
      self.idx = self.idx + steps
      ans = self.future[steps-1]
      self.future = self.future[steps:]
      return ans

  def url_str_print(self):
    print('url_str=====',self.url_str)
    print('future======', self.future)
    print('idx======',self.idx)


# Your BrowserHistory object will be instantiated and called as such:
browserHistory =BrowserHistory("leetcode.com")
browserHistory.visit("google.com")      # 你原本在浏览 "leetcode.com" 。访问 "google.com"
browserHistory.visit("facebook.com")     #// 你原本在浏览 "google.com" 。访问 "facebook.com"
browserHistory.visit("youtube.com")      #// 你原本在浏览 "facebook.com" 。访问 "youtube.com"
browserHistory.url_str_print()

print(browserHistory.back(1))                 #// 你原本在浏览 "youtube.com" ，后退到 "facebook.com" 并返回 "facebook.com"
browserHistory.url_str_print()

print(browserHistory.back(1))               #// 你原本在浏览 "facebook.com" ，后退到 "google.com" 并返回 "google.com"
browserHistory.url_str_print()
#
print(browserHistory.forward(1))               #// 你原本在浏览 "google.com" ，前进到 "facebook.com" 并返回 "facebook.com"
browserHistory.url_str_print()
browserHistory.visit("linkedin.com")     #// 你原本在浏览 "facebook.com" 。 访问 "linkedin.com"
print(browserHistory.url_str_print())
print(browserHistory.forward(2))              #// 你原本在浏览 "linkedin.com" ，你无法前进任何步数。
print(browserHistory.back(2))                   #// 你原本在浏览 "linkedin.com" ，后退两步依次先到 "facebook.com" ，然后到 "google.com" ，并返回 "google.com"
print(browserHistory.back(7)     )              #// 你原本在浏览 "google.com"， 你只能后退一步到 "leetcode.com" ，并返回 "leetcode.com"
