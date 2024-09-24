class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        line = left - 1
        right = len(matrix[line]) - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if matrix[line][mid] == target:
                return True
            if matrix[line][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False