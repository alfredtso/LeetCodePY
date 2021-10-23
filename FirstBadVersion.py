from typing import List

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        >>> s = Solution()
        >>> s.firstBadVersion(5)
        "hello"
        """
        lo = 0
        hi = n

        while (lo < hi) :
            mid = lo + (hi - lo) // 2
            result = isBadVersion(mid)

            if result:
                hi = mid
            else:
                if lo == mid:
                    return mid
                lo = mid


if __name__ == "__main__":
    import doctest
    doctest.testmod()

