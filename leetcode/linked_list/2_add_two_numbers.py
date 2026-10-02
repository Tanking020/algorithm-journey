class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 解法：
        # 时间复杂度：
        # 空间复杂度：


sol = Solution()
# —— 本地自测脚手架（力扣环境自带 ListNode，无需提交这段）——
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def build(arr):
#     """数组 -> 链表（力扣判题机就是这么把用例构造成输入的）"""
#     dummy = ListNode()
#     cur = dummy
#     for v in arr:
#         cur.next = ListNode(v)
#         cur = cur.next
#     return dummy.next
#
#
# def to_array(head):
#     """链表 -> 数组（方便和期望结果对照）"""
#     out = []
#     while head:
#         out.append(head.val)
#         head = head.next
#     return out
#
# l1 = build([2, 4, 3])                        # 表示数字 342（链表逆序存储）
# l2 = build([5, 6, 4])                        # 表示数字 465
# print(to_array(sol.addTwoNumbers(l1, l2)))   # 期望 [7, 0, 8]（即 807）
