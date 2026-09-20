class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result_set = set() # 结果数组用集合方式存储实现去重效果

        nums2_set = set(nums2) # 把 nums2 转成集合便于使用哈希表 查询 这个时间复杂度仅 O(1) 的快速操作

        for num in nums1:
            if num in nums2_set:
                result_set.add(num) # 集合是无序的,没有末尾添加的概念,因此集合的增操作是.add()
                
        return list(result_set)

sol = Solution()
print(sol.intersection([1,2,2,1],[2,2]))