
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.helper(l1,l2,0)

    def helper(self, l1, l2, carry):

        # either one None means unequal length, add leading zero e.g 999 + 099 = 1008
        if l1 == None and l2 != None:
            l1 = ListNode(0, next=None)
        elif l1 != None and l2 == None:
            l2 = ListNode(0, next=None)
        # ending case
        elif l1 == None and l2 == None and carry == 0:
            return
        # this is for cases like example 3 and the max value for carry is 1
        elif l1 == None and l2 == None and carry == 1:
            return ListNode(1, next=None)

        # Add both node and carry
        v = l1.val + l2.val + carry

        # to do: simplify this
        if v > 9:
            v = v % 10
            c = 1
        else:
            c = 0

        # recursion
        n = self.helper(l1.next, l2.next, c)

        # return the Head Node
        return ListNode(val=v, next=n)


    def test(self):
        three = ListNode(3, None)
        four = ListNode(4, three)
        two = ListNode(2, four)

        four2 = ListNode(4, None)
        six = ListNode(6, four2)
        five = ListNode(5, six)

        node = self.addTwoNumbers(two, five)
        print(f'The list is {node.val} -> {node.next.val} -> {node.next.next.val}')

    def carrytest(self):
        hun = ListNode(9, None)
        ten = ListNode(9, hun)
        digit = ListNode(9, ten)

        nine = ListNode(9, None)

        node = self.addTwoNumbers(digit, nine)
        print(f'The list is {node.val} -> {node.next.val} -> {node.next.next.val}->'
              f'{node.next.next.next.val}')


if __name__ == "__main__":
    my = Solution()
    my.test()
    my.carrytest()