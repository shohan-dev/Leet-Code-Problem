class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = sorted((nums1, nums2), key=len)
        m, n = len(A), len(B)
        half = (m + n + 1) // 2
        imin, imax = 0, m

        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i
            if i < m and A[i] < B[j-1]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
