class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 旧思路：暴力求解，但是这么做时间复杂度过高 经典的双层循环 时间复杂度 O(N^2)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[j] == target - nums[i]:
        #             result = [i,j]
        #             return result

        # 标准思路：使用哈希表进行空间换时间
        # 核心：哈希表的查找是O（1）,无论哈希表中有多少元素，要查出目标元素都只需要一次 也就是说我们把内层遍历 O（N）简化掉了
        hash_map = {} # 创建空哈希表

        for i,num in enumerate(nums): # 利用 enumerate() 得到元组（下标 i ，元素 num ），然后利用拆包操作对应到两变量

            diff = target - num

            if diff in hash_map: # 查询差值是否是哈希表中已经存在的键
                return [hash_map[diff],i] # 若差值已经是哈希表中的键，搜索成功，输出两数对应的下标
            
            hash_map[num] = i # 若差值不在哈希表中，则把 num 及其下标存进哈希表

        return [] # 保底机制，处理万一找不到符合条件的两数的情形

# 测试
sol = Solution()
print(sol.twoSum([2,6,8,1,3,5,7],7))