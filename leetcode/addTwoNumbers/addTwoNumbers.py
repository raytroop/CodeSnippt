# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and 
# each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        order = 1
        val_a = l1.val
        node_next = l1.next
        while(node_next):
            val_a += node_next.val * (10**order) 
            node_next = node_next.next
            order += 1
        
        order = 1
        val_b = l2.val
        node_next = l2.next
        while(node_next):
            val_b += node_next.val * (10**order) 
            node_next = node_next.next
            order += 1
        
        total = val_a + val_b
        vals = []
        mod = total % 10
        vals.append(mod)
        total = total // 10
        while(total):
            mod = total % 10
            vals.append(mod)
            total = total // 10

        list_node = []
        for val in vals:
            list_node.append(ListNode(val))
        for i in range(len(list_node) -1):
            list_node[i].next = list_node[i+1]
        return list_node[0]    


        

