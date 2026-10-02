class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # 回文链表 解法：快慢指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)

        # 利用快慢指针找中点，然后反转后半段
        # 平时遇到链表遍历不可假设其一定能走到 None, 要防止环的存在导致死循环
        # 单链表也可以有环，与定义不冲突
        # 不过力扣的链表题几乎全部由输入保证默认无环
        slow = head
        fast = head

        # 节点个数可能是奇数也可能是偶数
        # 慢指针：1 + k
        # 快指针：1 + 2 * k
        # [2 2 2 2] 偶数：快指针走到 None，慢指针正好走到中间偏右
        # [2 2 2 2 2 2]
        # [2 2 2 2 2] 奇数：快指针走到最后一个节点，慢指针正好走到中点
        # [2 2 2 2 2 2 2]

        # 待处理：空链表和单节点链表必定是回文链表
        # 此判定结束时候慢节点只会是中点或者中间偏右
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 从 slow 当前节点开始反转右半边
        prev = None
        current = slow

        # "None == prev <- node1(cur) | next_node == node2 -> node3 -> node4"
        # "None <- node1 <- node2 <- node3 <- node4"
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # 反转后后半部分链表的头节点是 prev
        # 开始从两头开始遍历逐个比对
        list1 = head
        list2 = prev

        # 注意到 list1 长度始终大于等于 list2
        # 偶数情形 list2 会提前抵达边界，所以 list1 剩余的中点不用管
        # 但还是对 list1 做判断进行安全兜底
        # 注意我【没有断开前半链表最后一个节点向后半链表尾部节点的指针】
        # 所以是偶数情形 list1 更长，奇数情形等长
        while list1 is not None and list2 is not None:

            # 比值，所以不用 is, 用 !=
            if list1.val != list2.val:
                return False

            # 先比较再移动
            list1 = list1.next
            list2 = list2.next

        return True

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

# 边界：长度 0 / 1 / 奇数 / 偶数，正例反例都要有
print(sol.isPalindrome(None))                   # 期望 True （空链表）
print(sol.isPalindrome(build([1])))             # 期望 True （单节点）
print(sol.isPalindrome(build([1, 1])))          # 期望 True
print(sol.isPalindrome(build([1, 2])))          # 期望 False
print(sol.isPalindrome(build([1, 2, 1])))       # 期望 True （奇数长度）
print(sol.isPalindrome(build([1, 2, 2, 1])))    # 期望 True （偶数长度）
print(sol.isPalindrome(build([1, 2, 3, 2, 1]))) # 期望 True （奇数长度）
print(sol.isPalindrome(build([1, 2, 3, 4, 1]))) # 期望 False
print(sol.isPalindrome(build([1, 1, 1, 1])))    # 期望 True
