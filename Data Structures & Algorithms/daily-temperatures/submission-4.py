class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, last_i = stack.pop()
                res[last_i] = i - last_i
            
            stack.append((temp, i))
        
        return res