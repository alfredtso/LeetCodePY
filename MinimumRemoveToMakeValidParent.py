"""

# tag::minMove
Test1::
    >>> my = Solution()
    >>> my.minRemoveToMakeValid("leet(t(c)o)de)")
    'lee(t(co)de)'
    >>> my.minRemoveToMakeValid("a)b(c)d")
    'ab(c)d'
    >>> my.minRemoveToMakeValid("))((")
    ''
    >>> my.minRemoveToMakeValid("(a(b(c)d)")
    'a(b(c)d)'

# end::minMove
"""

# tag::minMove
import collections

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = collections.deque([])
        rm_ls = set()

        for i, x in enumerate(s):
            if x not in "()":
                continue

            if x == "(":
                stack.append(i)
            elif x == ")":
                try:
                    stack.pop()
                except IndexError:
                    rm_ls.add(i)

        rm_ls = rm_ls.union(set(stack))
        string_builder = []

        for i, x in enumerate(s):
            if i not in rm_ls:
                string_builder.append(x)

        return "".join(string_builder)

# end::minMove

if __name__ == "__main__":
    import doctest

    doctest.testmod()