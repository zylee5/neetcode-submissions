class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2

        # points[l:i] -> distance <= pivot distance
        # points[i:j] -> distance > pivot distance
        # points[j]   -> current point being checked
        # points[r]   -> pivot
        def partition(l, r):
            pivot = points[r]
            pivotDist = euclidean(pivot)
            i = l
            for j in range(l, r):
                currDist = euclidean(points[j])
                if currDist <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        l, r = 0, len(points) - 1
        pivotIdx = len(points)
        while pivotIdx != k:
            pivotIdx = partition(l, r)
            if pivotIdx > k:
                r = pivotIdx - 1
            elif pivotIdx < k:
                l = pivotIdx + 1
        return points[:k]