class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # 解法：单调栈（栈内下标对应的温度，从栈底到栈顶【单调不增】）

        # 核心理解：每来一个新元素，就把 “破坏单调性的那些栈顶元素” 弹掉，用这种方式维持单调递减

        # 时间复杂度：O(n)，每个下标最多入栈一次、出栈一次，均摊 O(1)
        # 空间复杂度：O(n)，最坏情况（温度持续递减）栈里要存下所有下标

        # 题型总结：“最近的、比我大/小、左/右第一个” -> 单调栈
        # "配对/回退/撤销" -> 普通栈

        n = len(temperatures)
        stack = [] # 单调栈 只存下标（天数）
        result = [0] * n

        for i, t in enumerate(temperatures):
            # 新元素能处理栈顶（温度比栈顶更高）时不断处理栈顶并释放
            # 同时更新结果数组，只需下标相减符合直觉
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j

            # 栈空或新数已经不大于栈顶（栈中无新元素可处理的元素），才将新元素入栈待处理
            stack.append(i)

        return result

sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
