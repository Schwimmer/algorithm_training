#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    思路：
    另起两个链表，l3用于在扫描l1和l2的时候，判断next应该接在谁后面；
    l4用于指向l3的头，最后输出l4.next
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(None)
        l4 = l3
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1 
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        l3.next = l1 if l1 else l2
        return l4.next
        
# @lc code=end

