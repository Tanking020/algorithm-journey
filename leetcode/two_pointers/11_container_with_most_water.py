class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 盛最多水的容器问题
        # 双指针解法 时间复杂度 O(N), 空间复杂度 O(1)
        # 双指针移动过程中底边长度一定在缩小，所以想让容量(面积)变大只能是短板变长
        left = 0
        right = len(height) - 1
        result_area = 0

        while left < right:
            cur_length = right - left
            cur_short_height = min(height[left], height[right])
            cur_area = cur_length * cur_short_height

            # 若更新后面积更大，更新结果面积
            if cur_area > result_area:
                result_area = cur_area

            # 布置双指针移动规则: 谁是短板显然就应该移动谁
            # 都是短板的时候移动哪边都行，这里统一移动左边
            if height[left] <= height[right]:
                left += 1

            # 错误冗余规则删除:不需要布置两边一样高的情形
            # 因为它们都是短板，无论移动谁都必定被另一边的短板限制住

            # # 如果一样长, 优先移动: 移动后能带来更大收益的指针
            # elif height[left] == height[right]:

            #     if height[left + 1] > height[right - 1]:
            #         left += 1
            #     elif height[left + 1] < height[right - 1]:
            #         right -= 1
            #     else:
            #         left += 1
            #         right -= 1

            # 仔细思考后发现，相等(都是短板)时同时移动两指针是正确思路，能实现更高效的遍历
            # (去除了一部分无效遍历)(但并没改变时间复杂度量级)
            elif height[left] == height[right]:
                left += 1
                right -= 1

            else:
                right -= 1

        return result_area
# 测试
sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))