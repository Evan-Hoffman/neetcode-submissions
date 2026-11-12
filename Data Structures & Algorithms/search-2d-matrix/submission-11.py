class Solution:
    import math
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ##perform a binary search to find the row where target would be
        ## binary search within that row

        l, h = 0, len(matrix) - 1

        while l <= h:
            mid = (l + h) // 2

            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                h = mid - 1
            else:
                break

        mid = (l + h) // 2

        left, right = 0, len(matrix[mid]) - 1

        while left <= right:
            m = (left + right) // 2

            if matrix[mid][m] < target:
                left = m + 1
            elif matrix[mid][m] > target:
                right = m - 1
            else:
                return True
        
        return False































        # low, high = 0, len(matrix) - 1

        # while low <= high:
        #     mid = (low + high) // 2

        #     if matrix[mid][0] > target:
        #         high = mid - 1
        #     elif matrix[mid][-1] < target:
        #         low = mid + 1
        #     else:
        #         break
        
        # row = (low + high) // 2

        # low, high = 0, len(matrix[row]) - 1

        # while low <= high:
        #     mid = (low + high) // 2

        #     if matrix[row][mid] > target:
        #         high = mid - 1
        #     elif matrix[row][mid] < target:
        #         low = mid + 1
        #     else:
        #         return True
        
        # return False

        