class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        wordSet = set()

        def isWordStart(i, r, c) -> bool:
            ##check out of bounds or already used or wrong letter
            if (min(r, c) < 0 or r == ROWS or c == COLS
            or (r, c) in wordSet or board[r][c] != word[i]):
                return False

            ##check if last letter:
            if i == len(word) - 1:
                return True

            wordSet.add((r, c))
            ## recurisevly call for neighbors
            toRet = isWordStart(i + 1, r - 1, c) or isWordStart(i + 1, r + 1, c) or isWordStart(i + 1, r, c - 1) or isWordStart(i + 1, r, c + 1)

            wordSet.remove((r, c))
            return toRet

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if isWordStart(0, r, c):
                        return True

        return False

        