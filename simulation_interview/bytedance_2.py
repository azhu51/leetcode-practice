

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
      if not root: return True
      return self.isBalanced(root.left) and self.isBalanced(root.right) and \
             abs(self.helper(root.left) - self.helper(root.right)) <=1

    def helper(self, root):
      if not root: return 0
      return max(self.helper(root.left), self.helper(root.right)) + 1


from typing import  List

class SnakeGame:

  def __init__(self, width: int, height: int, food: List[List[int]]):
    """
    Initialize your data structure here.
    @param width - screen width
    @param height - screen height
    @param food - A list of food positions
    E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
    """
    from collections import deque
    self.track = deque()
    self.score = 0
    self.pos = [0, 0]
    self.width = width
    self.height = height
    self.food = food

  def move(self, direction: str) -> int:
    """
    Moves the snake.
    @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
    @return The game's score after the move. Return -1 if game over.
    Game over when snake crosses the screen boundary or bites its body.
    """
    d = {'U':(-1, 0), 'L':(0,-1), 'R':(0,1), 'D':(1,0)}
    step = d[direction]

    if self.track:

      temp = self.track.popleft()
      print("temp", temp)
      print("track", self.track)
    else:
      temp = self.pos

    self.pos = [self.pos[0] + step[0], self.pos[1] + step[1]]
    if self.pos in self.track or self.pos[0] < 0 or self.pos[
      0] >= self.height or self.pos[1] < 0 or self.pos[1] >= self.width:
      return -1

    else:
      if self.food != [] and self.pos == self.food[0]:
        self.score += 1
        self.food.pop(0)
        self.track.appendleft(temp)
        self.track.append(self.pos)
      else:
        self.track.append(self.pos)

    print(self.track)
    return self.score



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

sganme = SnakeGame(3,2,food = [[1,2],[0,1]])

print(sganme.move("R"))
print(sganme.move("D"))
print(sganme.move("R"))
print(sganme.move("U"))

