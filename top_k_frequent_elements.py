from heapq import *
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        heap = []
        for num, freq in num_freq.items():
            if len(heap) < k: 
                heappush(heap, (freq, num))
                continue
            if freq > heap[0][0]:
                heappushpop(heap, (freq, num))
        
        res = [0] * k
        for i in range(k -1, -1, -1):
            res[i] = heappop(heap)[1]
        return res

