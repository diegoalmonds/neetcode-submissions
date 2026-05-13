class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        heap = []
        for c in count.items():
            heapq.heappush(heap, (c[1], c[0]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res


