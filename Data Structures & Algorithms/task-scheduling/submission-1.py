class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ##create a counter out of tasks
        ##heapify as (-val, key)
        ## create an empty queue, a time var
        ## while heap and queue:
            ##pop max, if > 1, decrement freq and add to q with a time it will become availble 
            ##if not heap, set time to head of queue and continue
        
        freqs = collections.Counter(tasks)
        heap = [-val for val in freqs.values()]
        heapq.heapify(heap)

        q = collections.deque()
        time = 0

        while heap or q:
            time += 1

            if len(heap):
                freq = heapq.heappop(heap)
                if (freq * -1 > 1):
                    q.append((time + n, freq + 1))
            
            else:
                t, freq = q.popleft()
                time = t
                heapq.heappush(heap, freq)
            
            if q and q[0][0] == time:
                heapq.heappush(heap, q.popleft()[1])
        
        return time
            