class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqsArr = [[] for i in range(len(nums) + 1)]

        counter = Counter(nums)

        for num, ct in counter.items():
            freqsArr[ct].append(num)
        
        res = []
        while k:
            top = freqsArr.pop()
            if len(top):
                res.extend(top)
                k -= len(top)
        
        return res









        