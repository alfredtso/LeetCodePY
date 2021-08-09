import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = math.inf
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


        res = 0
        # Brute force: try every pair
        # for i in range(len(prices)):
            # for j in range(i + 1, len(prices)):
                # res = max(res, prices[j] - prices[i])

        # Non Brute force: recursive ?
        # use helper
        # return self.help(prices, math.inf, 0)

    def help(self, prices: List[int], num_to_be_add:int, max_sofar: int):
        if prices != []:
            if num_to_be_add < max(prices):
                max_sofar = max(max_sofar, max(prices)-num_to_be_add)
                return self.help(prices[1:], prices[0], max_sofar)
            else:
                return self.help(prices[1:], prices[0], max_sofar)
        else:
            return max_sofar


    def test(self):
        assert self.maxProfit([2,4,1]) == 2
        assert self.maxProfit([7, 1, 5, 3, 6, 4]) == 5
        assert self.maxProfit([7, 6, 4, 3, 1]) == 0


if __name__ == "__main__":
    my = Solution()
    my.test()
