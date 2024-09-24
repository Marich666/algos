class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m + n - 1
        j = n - 1
        k = m - 1
        while j >= 0:
            if k<0 or nums2[j] > nums1[k]:
                nums1[i] = nums2[j]
                j-=1
            else:
                nums1[i] = nums1[k]
                k-=1
            i-=1
        