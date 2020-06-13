
# https://leetcode-cn.com/problems/word-ladder-ii/

from typing import  List

# https://leetcode-cn.com/problems/word-ladder-ii/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you--2/
from collections import defaultdict
from collections import deque
import string
class Solution:


  def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:


    word_set = set(wordList)
    res = []
    if len(word_set) == 0 or endWord not in word_set:
      return res

    successors = defaultdict(set)

    found = self.__bfs(beginWord, endWord, word_set, successors)
    if not found:
      return res

    #print(successors)
    path = [beginWord]
    self.__dfs(beginWord, endWord, successors, path, res)
    return res

  def __bfs(self, beginWord, endWord, word_set, successors):
    queue = deque()
    queue.append(beginWord)

    visited = set()
    visited.add(beginWord)

    found = False
    word_len = len(beginWord)
    next_level_visited = set()

    while queue:
      current_size = len(queue)
      for i in range(current_size):
        current_word = queue.popleft()
        word_list = list(current_word)

        for j in range(word_len):
          origin_char = word_list[j]

          for k in string.ascii_lowercase:
            word_list[j] = k
            next_word = ''.join(word_list)

            if next_word in word_set:
              if next_word not in visited:
                if next_word == endWord:
                  found = True
                next_level_visited.add(next_word)
                queue.append(next_word)

                successors[current_word].add(next_word)
          word_list[j] = origin_char
      if found:
        break
          # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
      visited |= next_level_visited
      next_level_visited.clear()
    return found

  def __dfs(self, beginWord, endWord, successors, path, res):
    if beginWord == endWord:
      res.append(path[:])
      return

    if beginWord not in successors:
      return

    successor_words = successors[beginWord]
    for next_word in successor_words:
      path.append(next_word)
      self.__dfs(next_word, endWord, successors, path, res)
      path.pop()


s = Solution()
s.findLadders(beginWord = "hit",
    endWord = "cog",
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
)

