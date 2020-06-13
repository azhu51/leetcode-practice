
# -*- coding: utf-8 -*-
# @date     : 2020/6/12
# @author   : jawiezhu@tencent.com
# @version  : 1.0.0
# @summary  :

from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        if not A: return []

        ans = []
        A_1 = []
        A_2 = []
        for i in range(0, len(A)):
            if A[i] % 2 == 0:
                A_2.append(A[i])
            else:
                A_1.append(A[i])


        for p in range(0,len(A_1)):
            ans.append(A_2[p])
            ans.append(A_1[p])

        return ans


    def reverseWords(self, s: str) -> str:
        if not s: return ""
        ans = []
        for elem in s.strip().split(" "):
            if elem != "":
                ans.append(elem.strip())

        return " ".join(ans[::-1])

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target: return 0
        if startFuel < target and stations and startFuel < stations[0][0]: return -1

        restFuel = startFuel
        pos = 0
        res = 0
        import heapq
        heap = []
        while restFuel < target:
            for i in range(pos, len(stations)):
                if restFuel >= stations[i][0]:
                    # getFuel.append(stations[i][1])
                    heapq.heappush(heap, -stations[i][1])
                    pos += 1

            if restFuel < target:
                if not heap:
                    return -1
                restFuel -= heapq.heappop(heap)
                res += 1

        return res

    # dp
    def minRefuelStopsII(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)
        for i, d in enumerate(dp):
            if d >= target: return  i
        return -1







s = Solution()
s.sortArrayByParityII([4,2,5,7])
s.reverseWords("a good   example")
s.minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]])