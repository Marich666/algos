class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i, j = 0, 0
        while i<len(nums1) or j<len(nums2):
            if j>=len(nums2) or (i<len(nums1) and nums1[i] < nums2[j]):
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        if len(arr) % 2 == 0:
            res = (arr[(len(arr)//2)-1] + arr[len(arr)//2]) / 2
        else:
            res = arr[(len(arr) // 2)]
        return res

