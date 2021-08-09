from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        >>> sol = Solution()
        >>> ar = [4,5,6,7,0,1,2]
        >>> sol.search(ar, 0)
        4
        >>> sol.search(ar, 3)
        -1
        >>> sol.search([1], 0)
        -1
        >>> sol.search([1, 3], 3)
        1

        :param nums:
        :param target:
        :return:
        """

        res = -1
        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = (start + end) // 2

            # return immediately if lucky
            if nums[mid] == target:
                return mid
            # identify the 2 case, no equal case as the condition here is all unique
            # case 1: if the mid elm is larger than the first then first half is sorted
            # Further if target within this part -> trivial
            # if target no within ....
            elif nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            # case 2: if mid elm is smaller than the first then the second half is sorted
            elif nums[mid] < nums[start]:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                end -= 1


        return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()