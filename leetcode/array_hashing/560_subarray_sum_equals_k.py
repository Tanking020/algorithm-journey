class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 旧思路1:暴力枚举,时间复杂度 O(N^2) ,代码存在巨大BUG:过于希望代码符合条件时候提前终止,利用大于形式作判断,没有考虑负数情形
        # 实际上考虑得太复杂了,用等于判定就行
        # if not nums:
        #     return 0

        # son_list_num = 0

        # for i, num in enumerate(nums):
        #     # 如果 num 大于 k 直接空过
        #     # 如果 num 等于 k 它自身肯定算一个子数组,子数组个数加一
        #     if num == k:
        #         son_list_num += 1
        #     # 如果 num 小于 k 就要在它之后的元素里面去查询其他元素来凑和为 k 了 往后不断加直到加到大于 k 为止吧
        #     elif num < k:
        #         sum = num
        #         j = 1
        #         l = len(nums) - i - 1
        #         while sum < k and j <= l:
        #             sum += nums[i + j]
        #             j += 1
        #         if sum == k:
        #             son_list_num += 1

        # return son_list_num

        # 暴力枚举法修改版本:(但肯定不是真正好的方案)
        # count = 0
        # n = len(nums)
        
        # # 枚举所有起点
        # for i in range(n):
        #     total = 0
        #     # 从 i 开始往后累加
        #     for j in range(i, n):
        #         total += nums[j]
        #         if total == k:
        #             count += 1
        
        # return count

        # 更好的思路:前缀和 + 哈希表(时间复杂度:O(N))
        # 补充说明: 前缀和把“子数组求和”变成“累计和相减”，哈希表负责快速查找“前面有没有出现过某个累计和”
        prefix_sum_count = {0: 1} # 初始化 前缀和:计数 字典 {前缀和:出现次数}

        count = 0 # 和为 k 的子序列计数初始化
        prefix_sum = 0 # 初始化前缀和

        for num in nums:
            prefix_sum += num # 更新前缀和

            # prefix_sum_pre - prefix_sum_current = k 
            # 这也是用 前缀和 查询和为定值的子列的原因
            if prefix_sum - k in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k] # 加该前缀和对应计数的数量作为子序列数量

            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1 # 更新该前缀和对应计数

        return count

sol = Solution()
print(sol.subarraySum([1,1,1],2))