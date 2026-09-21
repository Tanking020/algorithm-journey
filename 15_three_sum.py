class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 固定一个 + 双指针 注意地位对称性 时间复杂度 O(N^2)
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n - 2): # 留两个位置给双指针
            if i > 0 and nums[i] == nums[i - 1]: # 跳过重复元素
                continue
            target = - nums[i]

            left = i + 1 # 核心，天然避开 i ，要注意 i, left, right 三个指针的地位等价意义(对称性)
            right = n - 1 # 双指针要在遍历内部重置，也就是说对每个元素用一次双指针

            while left < right:
                total = nums[left] + nums[right]

                if total == target:
                    # 注意：.append追加的是引用,如果用变量名过渡： list1 = [1，2，3]
                    # 然后list2.append(list1),那么 list1 重新赋值 ( list1 = [2,2,4]) 的时候，大列表中之前存入的 list1 也会同时被修改
                    # 最后得到的结果将会是 list2 = ([2,2,4],...,[2,2,4])
                    # 非要这么做的话要 .append 副本来避免因重新赋值带来的大列表错误变动
                    result.append([nums[i], nums[left], nums[right]]) # 所以说干脆不用中间变量名过渡就行了

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 # 跳过重复元素

                    # 题目要求无重复三元组，满足条件后这两指针可以同时移动了
                    # 因为只移动一个还能保持 == total 的话，说明本次单元素移动后元素值不变（重复）
                    left += 1
                    right -= 1 

                elif total < target:
                    left += 1
                elif total > target:
                    right -= 1

        return result

# 测试
sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))