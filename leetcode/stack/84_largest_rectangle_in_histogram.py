class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 解法：单调栈 (栈内下标对应的高度【非递减】)
        # 时间复杂度：O(n), 每个下标最多入栈一次，出栈一次
        # 空间复杂度：O(n), 最坏情况（高度持续递增）时栈里存下所有下标

        # 思路：最大矩形必定以某根柱子的高度为高，所以只需枚举每根柱子 i 当高度
        # 求它能向左右延伸多远
        
        # 如何同时获取某根柱子的左右边界（以它的高度为高，它在自己的区间内始终最矮）：
        # 栈内高度保持【非递减】：栈顶下面那个元素的高度必定 ≤ 栈顶高度
        # 也就是说，弹出栈顶 j 之后，新的栈顶就是 j 的【左边界】（它的高度 ≤ heights[j]）
        # 而右侧新探测到的柱子 h 严格矮于 j 的高度，所以当前下标 i 就是 j 的【右边界】
        # 左右边界都拿到 → 结算 j：宽度 = i - left - 1，两侧边界柱子本身不参与矩形构造

        # 等高情形：因为左边界是 ≤ 而右边界是 <，新栈顶可能与 j 等高，这时算出的宽度会偏小；
        # 但同一串等高的柱子中【最左那根】会拿到完整宽度，所以全局最大值不受影响

        stack = []
        heights = heights + [0] # 防止右边一直单增，布置哨兵作为边界
        max_area = 0

        # 每根柱子做两件事：① 自己入栈等待；② 若它比栈顶更矮，它就是栈顶的【右边界】→ 弹出栈顶并结算
        # 两种边界情形：栈空时左边界取 -1；末尾哨兵 0 会强制结算栈内剩余柱子
        for i, h in enumerate(heights):

            while stack and h < heights[stack[-1]]:
                j = stack.pop() # j 是正在被结算的柱子：它的左右边界刚刚确定

                # 栈空时说明左边界一路向左不停，用 -1 当作左边界，-1 下标同样不参与矩形构造
                left = stack[-1] if stack else -1
                max_area = max((i - left - 1) * heights[j], max_area) # 左右边界柱子不参与矩形构造, i 就是右边界

            stack.append(i)

        return max_area
    
sol = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))