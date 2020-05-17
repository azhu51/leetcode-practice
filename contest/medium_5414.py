
# https://leetcode-cn.com/contest/weekly-contest-189/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

from typing import List

class Solution:
  def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
    if not favoriteCompanies: return []
    res_set = set()
    set_list = []
    elem_set = set()


    for i in range(0, len(favoriteCompanies)):
      if len(favoriteCompanies[i]) == 1:
        res_set.add(repr(favoriteCompanies[i][0]))

    if len(res_set) == len(favoriteCompanies):
      return [i for i in range(0, len(res_set))]

    for i in range(0, len(favoriteCompanies)):
      for item in favoriteCompanies[i]:
        elem_set.add(item)
      set_list.append(elem_set)
      elem_set = set()
    #
    # res_list = []
    #
    # for i in range(0, len(set_list)):
    #   for j in range(i+1, len(set_list)):
    #     print(set_list[i], set_list[j], set_list[i].intersection(set_list[j]))
    #     if set_list[i].intersection(set_list[j]) == set():
    #       res_list.append(i)
    #       res_list.append(j)
    #     if(len(set_list[i]) > len(set_list[j]) and len(set_list[i].intersection(set_list[j])) < min(len(set_list[i]), len(set_list[j])))\
    #         :
    #       res_list.append(i)

    # tmp_companies = favoriteCompanies
    res_list = [i for i in range(0,len(favoriteCompanies))]
    sub_list = set()
    for i in range(0, len(set_list)):
      for j in range(i+1, len(set_list)):
        if set_list[j].intersection(set_list[i]):
          if len(set_list[j].intersection(set_list[i])) == len(set_list[j]) or \
              len(set_list[j].intersection(set_list[i])) == len(set_list[i]):
            if len(set_list[j]) < len(set_list[i]):
              sub_list.add(j)
            else:
              sub_list.add(i)

    res = []

    for item in sub_list:
      res_list[item] = -1
    for i in range(0, len(res_list)):
      if res_list[i] > -1:
        res.append(res_list[i])

    return res



s = Solution()
print(s.peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))
#print(s.peopleIndexes(favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]))
#print(s.peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))