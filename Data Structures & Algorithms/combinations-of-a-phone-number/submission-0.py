class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        digitsMap = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }

        res, curCombo = [], []

        def dfs(i):
            if i == len(digits):
                res.append("".join(curCombo))
                return
            
            for c in digitsMap[digits[i]]:
                curCombo.append(c)
                dfs(i + 1)
                curCombo.pop()
        
        dfs(0)
        return res
        