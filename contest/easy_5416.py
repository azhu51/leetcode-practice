
# https://leetcode-cn.com/contest/weekly-contest-190/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
  def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    if not searchWord: return -1
    ans_word = ""
    for word in sentence.split(" "):
      if word.startswith(searchWord):
        ans_word = word
        break
    if ans_word == "":
      return -1
    return sentence.split(" ").index(ans_word)+1
    # return sentence.split(" ")


s = Solution()
print(s.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))
