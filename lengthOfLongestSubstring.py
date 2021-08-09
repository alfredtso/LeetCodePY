import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        map = collections.defaultdict(int, {})

        # sliding window
        start = 0
        end = 0
        res = 0

        while end < len(s):

            # get the right end of  the "window" and add it to map
            char = s[end]
            map[char] += 1

            # check if the char at the right end is already in the map
            # If yes, delete the leftmost character from map since the window will slide right
            while map[char] > 1:
                leftmost_char = s[start]
                map[leftmost_char] -= 1
                start += 1

            res = max(res, end - start +1)


            end += 1

        return res




    def test(self):
        assert self.lengthOfLongestSubstring("abcabcbb") == 3
        assert self.lengthOfLongestSubstring("bbbbb") == 1
        assert self.lengthOfLongestSubstring("") == 0
        assert self.lengthOfLongestSubstring("pwwkew") == 3


if __name__ == "__main__":
    my = Solution()
    my.test()
