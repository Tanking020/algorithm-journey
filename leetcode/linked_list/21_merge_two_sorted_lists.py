class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 解法：dummy 哨兵 + 尾指针
        # 时间复杂度：O(m + n) # 两链表长度之和
        # 空间复杂度：O(1)
        # 这个方法按顺序串出新链表
        
        # 假头：消灭"新头是谁"和"空链表"两个边界
        dummy = ListNode()
        # 尾指针：一直指着【已合并部分的最后一个节点】
        # dummy 是新链表的入口，不能动（移动），因此需要 tail
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                # 把 list1 这个节点接到新链尾巴后面
                tail.next = list1
                # 旧链指针前进
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            # 尾巴前进（最容易漏）
            tail = tail.next

        # 退出时至少有一条已空，把剩下那条整段挂上
        tail.next = list1 if list1 is not None else list2

        # 返回 dummy.next 而不是 dummy ! dummy 是个假头
        # dummy.next 相当于 head
        return dummy.next

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

print(to_array(sol.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))))   # 期望 [1, 1, 2, 3, 4, 4]
