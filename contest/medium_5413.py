
# https://leetcode-cn.com/contest/weekly-contest-189/problems/rearrange-words-in-a-sentence/

class Solution:
  def arrangeWords(self, text: str) -> str:

    if not text: return ""
    text_list = []

    for s in text.lower().split(" "):
      text_list.append([s, len(s)])

    after_sort = sorted(text_list, key=lambda x: x[1])
    res = ""

    for i in range(0, len(after_sort)):
      if i == 0 :
        res = res + after_sort[0][0][0].upper()
        res = res + after_sort[0][0][1:]
        res = res + " "
      else:
        res = res + after_sort[i][0]
        res = res + " "

    return res[0:-1]

s = Solution()
print(s.arrangeWords(text = "Leetcode is cool"))