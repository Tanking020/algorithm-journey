class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # 解法：滑动窗口
        # 时间复杂度：O(n)，每个元素最多被左右指针各访问一次
        # 空间复杂度：O(1)，只用了常数个变量
        left = 0
        n = len(nums)
        cur_sum = 0
        result_length = float('inf') # 数列长度初始化为无穷大（因为后面是用 min() 来更新结果长度）

        for right in range(n):
            # # 错误思路：切片求和，这个操作时间复杂度是 O(N)
            # cur_sum = sum(nums[left:right + 1])

            # 实际采用边扩张边累加方法
            cur_sum += nums[right]
            
            while cur_sum >= target:
                # 此时都是满足条件的数组，用 min() 边收缩边不断更新结果数组长度
                result_length = min(right - left + 1, result_length)
                # left 收缩, 减去移除出窗口的元素
                cur_sum -= nums[left]
                left += 1

        return 0 if result_length == float('inf') else result_length

sol = Solution()
print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))