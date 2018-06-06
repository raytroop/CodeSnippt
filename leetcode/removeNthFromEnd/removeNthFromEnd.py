# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def traversal(self, head):
        """
        :type head: ListNode
        :rtype: List[ListNode]
        """
        res = [head]
        while head.next is not None:
            res.append(head.next)
        return res
# [1,2,3,4,5]
# 2
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None

        res = self.traversal(head)
        if 1 == len(res) and n == 1:
            return None

        if n == len(res):
            del res[0]
            return res[0]

        if n == 1:
            res[-2].next = None
            del res[-1]
            return res[0]
        
        res[-n-1].next = res[-n+1]
        del res[-n]
        return head


if __name__ == '__main__':
    node = ListNode(1)
    res = []
    res.append(node)
    print(res[0] is node)
    ax = [1,2,3]
    del ax[0]
    print(ax)
