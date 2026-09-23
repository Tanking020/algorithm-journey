class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter, defaultdict

        # defaultdict: 访问不存在的键时，自动创建并赋默认值( int 类型默认赋 0 )，不会报keyError
        window_dict = defaultdict(int)

        # target_dict = {}
        # for key in t:
        #     if target_dict[key]:
        #         target_dict[key] += 1
        #     else:
        #         target_dict[key] = 1

        # 上面这样过于麻烦，不如直接返回计数字典
        need_dict = Counter(t)

        left = 0
        formed = 0 # 记录已经满足计数的元素的个数，避开使用两字典相等的判定
        length_result = float('inf')
        char_result = ""

        for right in range(len(s)):
            window_dict[s[right]] += 1

            if s[right] in need_dict and window_dict[s[right]] == need_dict[s[right]]: 
                # 存在性判断很重要，从不够到刚好够才 + 1 ，避免 formed 虚高
                formed += 1

            while formed == len(need_dict): # 检验已满足字符类别数量是否达标

                # 在 while == 内更新结果，因为这个循环内全是满足条件的，随时可能达到最短
                # 收缩后可能就不满足了，因此必须在收缩前(仍然满足条件)时更新结果
                if right - left + 1 < length_result:
                    char_result = s[left: right + 1]
                    length_result = right - left + 1

                # 收缩窗口，同时检测是否发生从满足到不满足的字符类别
                window_dict[s[left]] -= 1

                if s[left] in need_dict and window_dict[s[left]] < need_dict[s[left]]:
                    # 同理，别漏掉存在性判断导致在不必要的时候更新 formed
                    formed -= 1

                left += 1

        return char_result

sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
print(sol.minWindow("a", "aa"))