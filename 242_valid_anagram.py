class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 旧思路:1.使用了排序函数，时间复杂度 O(NlogN) ,不满足时间复杂度要求 O(N) 2.没有进行长度判别来提前剪枝
        # s_t = tuple(sorted(s))
        # t_t = tuple(sorted(t))

        # return s_t == t_t

        # 更好的思路：利用对序列计数函数 Counter ，仅用 O(N) 时间复杂度直接判断两字符串（序列）
        if len(s) != len(t):
            return False

        from collections import Counter
        count1 = Counter(s) # 直接统计字符串中各个元素的出现次数，时间复杂度 O(N)
        count2 = Counter(t)

        return count1 == count2

        # # 还有一种思路：注意这种思路的最坏时间复杂度是 O(N^2) ,虽然在特定数据集下可能更快但这是假快
        # # 力扣的毫秒数受测试数据影响，不能作为判断算法优劣的标准
        # if len(s) != len(t):
        #     return False

        # for char in s:
        #     if s.count(char) != t.count(char): # 这样做的好处是当某元素出问题时候直接返回不用过剩下的了
        #         return False

        # return True

sol = Solution()
print(sol.isAnagram("haha","ahah"))