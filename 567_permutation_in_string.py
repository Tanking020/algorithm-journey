class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 滑动窗口 + formed 满足变量
        # 时间复杂度：O(N) 空间复杂度：O(M)
        # leetcode 时间测试不够快，一方面是因为 Counter构建慢，另一方面defaultdict每次访问不存在的键都要走默认逻辑
        # 不过这并不影响 formed 是一个高效的算法
        # 如果字符集固定（比如小写字母），可以用长度为 26 的数组替代 defaultdict，速度会快很多
        from collections import Counter, defaultdict
        left = 0
        window = defaultdict(int)
        need = Counter(s1)
        formed = 0
        required = len(need) # 注意这里是字符种类数，要用 need 去重！不能直接用 len(s1) 哦

        for right in range(len(s2)):
            # 扩张同时更新窗口字典(增)
            window[s2[right]] += 1

            # 扩张后收缩前，判定满足变量增长
            if s2[right] in need and window[s2[right]] == need[s2[right]]:
                formed += 1

            # 这是一个变量更新疏漏，我已经犯了两次，这样先定义变量然后用变量判定却不更新变量会导致 while > 判定死循环！
            # window_length = right - left + 1
            # while window_length > len(s1):

            # 为避免这个重大的先定义变量参与判定却不更新变量的问题，一定要注意 while 循环做好条件变量更新即结束判定
            # 可以像这样干脆不前置变量，也可以在 while 内做好变量更新
            while right - left + 1 > len(s1):

                # 收缩循环中，每次收缩前，(使用旧的将被排除的 left )判定满足变量减小
                if s2[left] in need and window[s2[left]] == need[s2[left]]:
                    formed -= 1

                # 收缩循环中，每次收缩前更新窗口字典(减)
                window[s2[left]] -= 1

                # 收缩窗口
                left += 1

            if formed == required: 
                return True

        return False

sol = Solution()
print(sol.checkInclusion("ab","eidbaooo"))