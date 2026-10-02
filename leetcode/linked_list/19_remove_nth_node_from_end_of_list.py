class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
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
# print(to_array(sol.removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)))   # 期望 [1, 2, 3, 5]
