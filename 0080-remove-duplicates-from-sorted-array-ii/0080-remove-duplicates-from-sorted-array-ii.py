class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1
        isTwo = False
        for i in range(1, len(nums)):
            if nums[i] == nums[k-1]:
                if not isTwo:
                    nums[k] = nums[i]
                    k += 1
                    isTwo = True
            else:
                nums[k] = nums[i]
                k += 1
                isTwo = False
        return k