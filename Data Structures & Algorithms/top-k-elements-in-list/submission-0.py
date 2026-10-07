class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            result[num] = result.get(num,0)+1

        heap = []
        for nums in result.keys():
            heapq.heappush(heap,(result[nums],nums))
            if len(heap) > k:
                heapq.heappop(heap)
        final = []
        for i in range(k):
            final.append(heapq.heappop(heap)[1])
        return final


        