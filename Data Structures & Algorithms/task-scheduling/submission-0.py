class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                # execute the most frequent available task
                remainingCnt = -heapq.heappop(maxHeap) - 1
                if remainingCnt > 0:
                    readyTime = time + n
                    q.append((readyTime, remainingCnt))
            else:
                # jump to when the next task becomes available
                time = q[0][0]
            
            if q and q[0][0] == time:
                # cooldown finished, task is available again
                _, remainingCnt = q.popleft()
                heapq.heappush(maxHeap, -remainingCnt)
        return time