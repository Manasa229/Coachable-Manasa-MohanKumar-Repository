"""767. Reorganize String"""
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        For each character in the string, we can store the count as key in the dictionary and
        add them to max heap. Then we can take the top most occurring character and build a string
        and put them back to the heap with the updated count. If we are left with only one character in the
        heap, we can return empty string
        """
        freq = {}

        for char in s:
            freq[char] = 1 + freq.get(char, 0)

        heap = []
        for char, key in freq.items():
            heap.append((-key, char))

        heapq.heapify(heap)
        res = []

        while len(heap) > 0:
            count1, char1 = heapq.heappop(heap)
            if len(heap) == 0 and count1 < -1:
                return ""
            else:
                res.append(char1)
                if len(heap) > 0:
                    count2, char2 = heapq.heappop(heap)
                    res.append(char2)
                    if count2 < -1:
                        heapq.heappush(heap, (count2 + 1, char2))

                if count1 < -1:
                    heapq.heappush(heap, (count1 + 1, char1))

        return "".join(res)