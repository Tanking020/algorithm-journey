class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 对时间复杂度无要求，空间复杂度要求 O(1)
        # numbers 整数数组下标从 1 开始，按非递减顺序排列
        # 由于空间复杂度要求严格，这里就不用哈希表查询了
        
        # # 旧思路: 使用双层循环，时间复杂度 O(N^2)，空间复杂度 O(1)，能用但不够好
        # if not numbers:
        #     return []

        # n = len(numbers)
        # for index1 in range(n):
        #     diff = target - numbers[index1]
        #     for index2 in range(index1 + 1,n):
        #         if numbers[index2] == diff and index2 != index1:
        #             return [index1 + 1, index2 + 1]

        # return []

        # 更好的思路：使用双指针，时间复杂度 O(N), 空间复杂度 O(N)
        # 从题目说按非递减顺序排列就应该想到这一点
        # 注意题目要求下标从 1 开始，但是 py 中列表下标还是从 0 起的 
        left = 0
        right = len(numbers) - 1

        # left < right 条件判断天然排除了数组中元素个数小于等于 1 的情形 无需额外剪枝
        while left < right: # 题目要求不能同个位置元素加两次(重复使用相同的元素)，也就是输出不允许 left == right
            num_sum = numbers[left] + numbers[right]
            if num_sum == target:
                return [left + 1, right + 1]
            elif num_sum < target:
                left += 1
            else:
                right -= 1

        return[]
            
            
# 测试
sol = Solution()
print(sol.twoSum([2,7,11,5],9))