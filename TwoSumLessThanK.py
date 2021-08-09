from typing import List


class Solution:
    # return the maximum sum s.t there exist `i<j` with num[i] + num[j] = sum and sum < k, if none, -1
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        # maximum:
        max = -1

        # not sorted but i < j

        # approach 1: brute force
        for i in range(len(nums)):
            # check if less than k and > max
            for j in range(i+1, len(nums)):
                tmp = nums[i] + nums[j]
                # the best we can achieve, so return immediately
                if tmp == k-1:
                    return tmp
                elif k > tmp > max:
                    max = tmp

        # max must be < k-1, otherwise returned already
        return max

    def counting(self, nums: List[int], k:int) -> int:
        ans = -1
        # counting sort, first populate a array
        # Use the fact that nums[i] has constraints, make it 1-indexed with extra space
        count = [0]*1001

        # populate count with nums[i]
        for x in nums:
            count[x] += 1

        lo = 1
        hi = 1000

        while lo <= hi:
            sum = lo+hi

            # case 1: decrement hi or if nums doesn't contain hi
            if sum >= k or count[hi] == 0:
                hi = hi-1
            # case 2: sum < k, so we should increase lo; check if nums contain lo; further check if lo=hi
            else:
                if count[lo] > (0 if lo < hi else 1):
                    ans = max(ans, sum)

                lo +=1

        return ans





    def test(self):
        assert self.twoSumLessThanK([34,23,1,24,75,33,54,8], 60) == 58
        assert self.twoSumLessThanK([10, 20, 30], 15) == -1
        assert self.twoSumLessThanK([358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549],
1800) == 1794
        assert self.counting([34,23,1,24,75,33,54,8], 60) == 58
        assert self.counting([10, 20, 30], 15) == -1
        assert self.counting([358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549],
                             1800) == 1794


if __name__ == '__main__':
    my = Solution()
    my.test()
