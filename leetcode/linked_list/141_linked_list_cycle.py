class Solution(object):
    def hasCycle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
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
# a = build([3, 2, 0])
# a.next.next.next = a.next      # 尾节点 0 指回 2，形成环（入口为 2）
# print(sol.hasCycle(a))         # 期望 True
