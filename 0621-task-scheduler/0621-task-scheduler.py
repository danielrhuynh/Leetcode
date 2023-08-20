class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Each task 1 unit time
        # Minimize idle time
        
        count = Counter(tasks)
        maxHeap = [-ct for ct in count.values()] # Inverting pos vals to neg
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # Pairs of [-ct, idleTime]
        
        while maxHeap or q:
            time  += 1
            if maxHeap:
                ct = heapq.heappop(maxHeap) + 1
                if ct:
                    q.append([ct, n+time])
            if q and q[0][1] <= time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        