class Solution(object):
    def hasCycle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # 解法：快慢指针
        # 看到「判环 / 找中点 / 找倒数第 k 个」→ 条件反射想到【让两个指针速度不同】
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        slow = head
        fast = head

        # 快指针需要一下移动两格，因此对它进行越界限制
        # 而且这样也规避了空链表和单节点的情形，无需额外写提前返回
        while fast is not None and fast.next is not None:
            # 先移动后比较
            slow = slow.next
            fast = fast.next.next

            # is 判定身份（内存地址 id()）无法被改写
            # == 调用 __eq__，没定义就退化为 is，可以被类改写
            # 链表题判节点必须用 is（语义正确，免疫改写，更快（不走 __eq__ 调用））
            if slow is fast:
                return True

        return False

sol = Solution()
# —— 本地自测脚手架（力扣环境自带 ListNode，无需提交这段）——
class ListNode(object):
    # next 加类型注解：不加的话 Pylance 会推断成"永远是 None"，后面造环写不了
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
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

# 有环用例：3 -> 2 -> 0 -> 2 -> ...（尾节点 0 指回 2，环入口为 2）
n3, n2, n0 = ListNode(3), ListNode(2), ListNode(0)
n3.next, n2.next, n0.next = n2, n0, n2
print(sol.hasCycle(n3))         # 期望 True

# 无环用例：这三个边界最容易漏，务必都测
print(sol.hasCycle(None))              # 期望 False（空链表）
print(sol.hasCycle(ListNode(1)))       # 期望 False（单节点）
print(sol.hasCycle(build([1, 2, 3])))  # 期望 False（无环多节点）
