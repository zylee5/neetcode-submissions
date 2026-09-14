class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        stored = self.map.get(key)
        if not stored:
            return ""
        left, right = 0, len(stored) - 1
        while left <= right:
            mid = (left + right) // 2
            ts = stored[mid][1]
            if ts == timestamp:
                return stored[mid][0]
            elif ts < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        # All stored timestamps are greater than the requested timestamp        
        if right < 0:
            return ""
        
        return stored[right][0]
