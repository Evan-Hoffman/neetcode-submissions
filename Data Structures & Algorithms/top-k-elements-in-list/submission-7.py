class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for i in range(len(nums))]

        counter = Counter(nums)

        for num, ct in counter.items():
            freqs[ct - 1].append(num)
                
        result = []

        i = len(nums) - 1

        while len(result) < k:
            if len(freqs[i]):
                result.extend(freqs[i])
            
            i -= 1
        
        return result




        