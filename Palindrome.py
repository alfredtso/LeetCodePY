class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def test(self):
        assert self.isPalindrome(121) == True
        assert self.isPalindrome(-121) == False
        assert self.isPalindrome(10) == False


if __name__ == '__main__':
    my = Solution()
    my.test()
