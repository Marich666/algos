class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        count = 0
        pointer = 0
        best = nums[0]
        while pointer + best < len(nums) - 1:
            best = max(best, nums[pointer])
            b = best
            for i in range(1, best+1):
                best = max(best - 1, nums[pointer+i])
            count+=1
            pointer += b
        return count+1