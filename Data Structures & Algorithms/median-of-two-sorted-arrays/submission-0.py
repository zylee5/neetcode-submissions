class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Make sure A is the shorter array
        if len(B) < len(A):
            A, B = B, A

        # Binary search on A only (find partition)
        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2
            # Number of elements from A's left + B's left = half
            # (i + 1) + (j + 1) = half
            # i + j + 2 = half
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # Cross checking the partitions
            # All left <= all right
            # Only need to check these two (A and B are already sorted)
            if Aleft <= Bright and Bleft <= Aright:
                # Odd/even length
                if total % 2 != 0:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                # A's partition is too far right
                right = i - 1
            else:
                # A's partition is too far left
                left = i + 1