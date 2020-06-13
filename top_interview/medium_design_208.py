
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/

class Trie:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.corpus = []

  def insert(self, word: str) -> None:
    """
    Inserts a word into the trie.
    """
    self.corpus.append(word)

  def search(self, word: str) -> bool:
    """
    Returns if the word is in the trie.
    """
    if not self.corpus: return False
    if word in self.corpus:
      return True
    else:
      return False

  def startsWith(self, prefix: str) -> bool:
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
    if not self.corpus: return False
    for i in range(0, len(self.corpus)):
      if self.corpus[i][0:len(prefix)] == prefix:
        return True

    return False


# Your Trie object will be instantiated and called as such:
word = "apple"
prefix = "appd"
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
print(param_2)
param_3 = obj.startsWith(prefix)
print(param_3)

from collections import defaultdict


class TrieNode:
  def __init__(self):
    self.children = defaultdict(TrieNode)
    self.is_word = False


class Trie(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = TrieNode()

  def insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    cur = self.root
    for letter in word:
      cur = cur.children[letter]
    cur.is_word = True

  def search(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    cur = self.root
    for letter in word:
      cur = cur.children.get(letter)
      if cur is None:
        return False
    return cur.is_word

  def startsWith(self, prefix):
    """
    Returns if there is any word in the trie that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    cur = self.root
    for letter in prefix:
      cur = cur.children.get(letter)
      if cur is None:
        return False
    return True