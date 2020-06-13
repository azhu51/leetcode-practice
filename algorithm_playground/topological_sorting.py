

# https://www.runoob.com/python3/python-topological-sorting.html


from collections import defaultdict


# （1）拓扑排序并不唯一
# （2）不含回路的有向图（有向无环图）——一定存在拓扑排序。

# 归简法求解拓扑排序，第一直觉是先移除其中一个节点（后面会说，每次移除的都是当前拓扑结构中的入度为零的点，
# 入度为 0 的含义不依赖其他任何节点，即可发生），
# 然后解决其余 n-1 个节点的问题。

def topsort(G):
  in_degrees = dict((u, 0) for u in G)
  for u in G:
    for v in G[u]:
      in_degrees[v] += 1

  print(in_degrees)
  Q = [u for u in G if in_degrees[u] == 0]

  S = []

  while Q:
    u = Q.pop()
    S.append(u)
    for v in G[u]:
      in_degrees[v] -= 1

      if in_degrees[v] == 0:
        Q.append(v)

  return S


G = {
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''
}

print(topsort(G))


class Graph:
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def topoSortUtil(self, v, visited, stack):
    visited[v] = True

    for i in self.graph[v]:
      if visited[i] == False:
        self.topoSortUtil(i, visited, stack)

    stack.insert(0, v)

  def topoSort(self):
    visited = [False] * self.V
    stack = []

    for i in range(self.V):
      if visited[i] == False:
        self.topoSortUtil(i, visited, stack)

    print(stack)


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print("拓扑排序结果：")
g.topoSort()
