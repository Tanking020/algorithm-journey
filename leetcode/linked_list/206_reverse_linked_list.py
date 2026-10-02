class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 解法：
        # 时间复杂度：
        # 空间复杂度：
        if head is None or head.next is None:
            return head

        prev = None
        # leetcode 里把链表头当参数传进来了，Solution 类里没有 head 属性
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # leetcode 只给节点类，没有定义容器类，所以需要改头时不要动参数
        # 用 prev/dummy 记录，最后 return 出去
        return prev

sol = Solution()
# —— 本地自测脚手架（力扣环境自带 ListNode，无需提交这段）——
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(arr):
    """数组 -> 链表（力扣判题机就是这么把用例构造成输入的）"""
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_array(head):
    """链表 -> 数组（方便和期望结果对照）"""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


head = build([1, 2, 3, 4, 5])
print(to_array(sol.reverseList(head)))      # 期望 [5, 4, 3, 2, 1]
