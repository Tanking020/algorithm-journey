class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 固定多个 + 双指针 解法 在三数之和基础上的拓展
        # 时间复杂度：O(N^3)
        n = len(nums)
        nums.sort()
        result = []

        for index1 in range(n - 2): # 依旧留两个位置给双指针
            # 遇到重复情形直接跳过
            # 由于 index1 是从左往右遍历，不约束右边界处理直接向后检查可能遇到 index1 + 1 不存在的情形（越界）
            # 所以向前检查并且约定左边界处理
            if index1 > 0 and nums[index1] == nums[index1 - 1]:
                continue

            for index2 in range(index1 + 1, n - 2):
                if index2 > index1 + 1 and nums[index2] == nums[index2 - 1]:
                    continue

                num_sum1 = nums[index1] + nums[index2]
                two_target = target - num_sum1

                left = index2 + 1 # 避开重复（依旧是借助对称性质）
                right = n - 1
                while left < right:
                    num_sum2 = nums[left] + nums[right]

                    if num_sum2 == two_target:
                        result.append([nums[index1], nums[index2], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif num_sum2 < two_target:
                        left += 1

                    elif num_sum2 > two_target:
                        right -= 1

        return result

# 测试
sol = Solution()
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
print(sol.fourSum([2, 2, 2, 2, 2], 8))