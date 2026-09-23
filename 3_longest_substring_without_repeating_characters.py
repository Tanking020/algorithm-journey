class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 双指针滑动窗口解法
        # 时间复杂度 O(N) , 空间复杂度 O(N)
        left = 0
        n = len(s)
        seen_set = set() # seen_set 是窗口的镜像，记录窗口中有哪些元素方便查询

        result_length = 0

        # 注意无重复的含义不是相邻相等而是整个字符串中无重复元素
        # 看到这类窗口内重复检测可以第一时间想想集合
        # 答案并不需要输出序列本身，只要输出长度，所以两指针之间不需要是最长无重复序列本身(虽然我写的这段代码其实就是本身)！
        # 先制作指针移动规则，再加入结果更新规则

        for right in range(n):

            while s[right] in seen_set:
                # 右指针扫到重复元素时候循环在 seet_set 中删除左指针元素
                # 这样 while 会循环到左指针越过右指针当前重复元素为止(开启下个序列研究)
                # 右指针会把这个重复末端元素也就是下个序列的起始元素放进集合并且继续向右遍历
                seen_set.remove(s[left]) 
                left += 1

            # 右指针扫到的是窗口中没有过的元素的时候，用 seen_set 记录新元素
            seen_set.add(s[right])

            # 窗口稳定，布置更新策略
            # 不放在 while in 这个换下个序列操作期间
            result_length = max(right - left + 1, result_length)

        return result_length

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))