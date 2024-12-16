"""1405. Longest Happy String"""

import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        - Store the values in min heap
        -Pop the heap and form a string
            -If the string length if lesser than 2 or if its greater than 2 and the last char is not equal to the cur char that we are tring to add and not equal to the -2 positioned char, then add the cur char and decrement value in heap
            -If the length of the heap is 1 and dont match the condition, break
        -return res string

        Time Complexity:O(nlogn)
        Space Complexity:O(n)

        """
        res = []
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))

        if b > 0:
            heapq.heappush(heap, (-b, "b"))

        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        while len(heap) > 0:
            count, cur_char = heapq.heappop(heap)
            count2 = 0

            while (len(res) < 2 or (len(res) > 1 and (res[-2] != cur_char or res[-1] != cur_char))) and count < 0:
                res.append(cur_char)
                count += 1

            if len(res) > 1 and res[-2] == cur_char and len(heap) > 0:
                count2, char2 = heapq.heappop(heap)
                if (res[-1] != char2 or res[-2] != char2) and count2 < 0:
                    res.append(char2)
                    count2 += 1

            if count < 0:
                heapq.heappush(heap, (count, cur_char))

            if count2 < 0:
                heapq.heappush(heap, (count2, char2))

            if len(heap) == 1 and res[-1] == cur_char and res[-2] == cur_char:
                break

        return "".join(res)