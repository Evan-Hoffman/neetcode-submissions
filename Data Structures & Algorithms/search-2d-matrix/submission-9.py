class Solution:
    import math
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ##perform a binary search to find the row where target is greater than or equal to first element, less than next rows first element
        ## binary search within that row

        l, h = 0, len(matrix) - 1

        while l <= h:
            mid = (l + h) // 2

            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                h = mid - 1
            else:
                left, right = 0, len(matrix[mid])

                while left <= right:
                    m = (left + right) // 2

                    if matrix[mid][m] < target:
                        left = m + 1
                    elif matrix[mid][m] > target:
                        right = m - 1
                    else:
                        return True
                
                break
        
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ## implement a binary search on the first val of each row
        ## find the row where target is great than the first entry but less than the first entry of row + 1
        ## perform a binary search within that target row

        # lo, hi = 0, len(matrix) - 1

        # while lo < hi:
        #     mid = (lo + hi) // 2

        #     if matrix[mid][0] > target:
        #         hi = mid - 1
        #     elif matrix[mid][-1] < target:
        #         lo = mid + 1
        #     else:
        #         break
        
        # row = (lo + hi) // 2

        # lo, hi = 0, len(matrix[row]) - 1

        # while lo <= hi:
        #     mid = (lo + hi) // 2
        #     val = matrix[row][mid]

        #     if val > target:
        #         hi = mid - 1
        #     elif val < target:
        #         lo = mid + 1
        #     else:
        #         return True
        
        # return False
        
        

































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

        