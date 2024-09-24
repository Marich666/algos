class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for i in range(0, k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)