class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == '-':
            y = int(f'-{str(x)[-1:0:-1]}')

        else:
            y = int(str(x)[::-1])

        if y < -2**31 or y > 2**31 - 1:
            print("outside range")
            return 0
        else:
            print(y)
            return y

    def test(self):
        assert self.reverse(-2546) == -6452
        assert self.reverse(1534236469) == 0


if __name__ == '__main__':
    my = Solution()
    my.test()
