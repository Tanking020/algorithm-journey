class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 操作降低到O(N)时间复杂度的核心：借助哈希表 查询 操作的O(1)时间复杂度
        if not nums:
            return 0 # 边界情形检查，数组为空直接返回0

        num_set = set(nums) # 核心操作：利用集合化来去除重复元素

        max_length = 0 # 记录最长连续序列的长度

        for num in num_set:
            # 如果 num - 1 在集合中，说明 num 不是连续序列的起点，直接空过
            if num - 1 not in num_set:
                # 如果num - 1 不在集合中，说明 num 是连续序列的起点，开始计算连续序列长度
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set: # 利用while条件循环不断查询连续序列下一个元素是否存在于集合并不断更新元素和当前连续序列长度
                    current_num += 1
                    current_length += 1

                max_length = max(max_length,current_length) # 更新最大长度（使用max(),是O(1)操作）注意这一句要放进 if 判断中，有current_length时候才更新

        return max_length

# 测试
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))