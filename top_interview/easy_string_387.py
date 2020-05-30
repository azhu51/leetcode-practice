
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/

class Solution:
  def firstUniqChar(self, s: str) -> int:
    tmp_map = {}

    for c in s:
      if c not in tmp_map:
        tmp_map[c] = 1
      else:
        tmp_map[c] = tmp_map[c] + 1


    for c in s:
      if tmp_map[c] == 1:
        return s.index(c)

    return -1

