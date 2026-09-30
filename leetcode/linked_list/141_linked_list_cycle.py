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
# a, b, c = ListNode(3), ListNode(2), ListNode(0)
# a.next, b.next, c.next = b, c, b     # 让 c 指回 b 形成环
# print(sol.hasCycle(a))
