class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = -stones[i]
            
        maxHeap = stones
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, y-x)
        return -maxHeap[0] if maxHeap else 0