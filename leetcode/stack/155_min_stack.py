# class MinStack(object):

#     def __init__(self):
#         # 解法：双栈（主栈 + 辅助最小值栈）
#         # 时间复杂度：所有操作均为 O(1)
#         # 空间复杂度：O(n)，辅助栈最坏与主栈等长
#         # 因为力扣特意说了.pop等操作只在非空栈上调用，所以不用做非空 if 判定
#         self.stack = [] # 主栈：照常保存所有元素，只负责后进先出
#         self.min_stack = [] # 辅助栈：与主栈等长，记录每一层为止的最小值

#     def push(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         # 将元素 val 推入堆栈
#         self.stack.append(val) # 元素照常入主栈

#         # 辅助栈同步压入到目前为止的最小值
#         # 辅助栈为空时直接压入，新元素更小就用它，否则沿用上一层的最小值
#         if not self.min_stack or val < self.min_stack[-1]:
#             self.min_stack.append(val)
#         else:
#             self.min_stack.append(self.min_stack[-1])

#     def pop(self):
#         """
#         :rtype: None
#         """
#         # 删除堆栈顶部的元素
#         self.stack.pop()
#         self.min_stack.pop() # 辅助栈同步弹出，最小值自动回退到上一层

#     def top(self):
#         """
#         :rtype: int
#         """
#         # 获取堆栈顶部的元素
#         return self.stack[-1]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         # 这一步是核心：用 min 时间复杂度超标，用 sort 会破坏栈的意义
#         return self.min_stack[-1] # 辅助栈顶即当前最小值，O(1)

#     # 辅助栈要和主栈等长的原因：如果只存一个全局最小值，pop 掉它之后就不知道之前的最小值是多少了
#     # 辅助栈 每层都记 的做法天然解决这个 "回退" 问题

# 使用单栈思路再写一遍：
class MinStack(object):

    def __init__(self):
        # 解法：单栈 + 元组（每格同时存"元素值"和"到这一格为止的最小值"）
        # 时间复杂度：所有操作 O(1)
        # 空间复杂度：O(n)
        # 因为力扣特意说了.pop等操作只在非空栈上调用，所以不用做非空 if 判定
        self.stack = [] # 每格是一个元组 (val, cur_min)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # 三元表达式写法
        # prev_min = self.stack[-1][1] if self.stack else float('inf') # 解包给变量命名的写法增加可读性
        # cur_min = min(prev_min, val)

        # 也可以这么写：
        cur_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, cur_min))
        
    def pop(self):
        """
        :rtype: None
        """
        # 最小值跟格子绑定，格子被弹走，它携带的最小值信息也一起走了
        # 天然回退，不像辅助栈写法需要维护两个栈的同步
        self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())  # -3
# minStack.pop()
# print(minStack.top())     # 0
# print(minStack.getMin())  # -2