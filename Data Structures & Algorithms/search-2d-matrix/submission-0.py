class Solution:
    import math
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## implement a binary search on the first val of each row
        ## find the row where target is great than the first entry but less than the first entry of row + 1
        ## perform a binary search within that target row

        low, high = 0, len(matrix) - 1

        row = -1

        while low < high:
            mid = math.ceil((low + high) / 2)

            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][0] < target:
                low = mid
            else:
                return True
        
        row = high

        low, high = 0, len(matrix[row]) - 1

        while low <= high:
            mid = (low + high) // 2

            if matrix[row][mid] > target:
                high = mid - 1
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                return True
        
        return False

        