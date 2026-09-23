class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 滑动窗口法
        # 时间复杂度 O(N) , 空间复杂度 O(M)
        # 判定异位词的方法很关键，直接 window_dict == need_dict 不行，会因 defaultdict(int) 残存的 0 导致误判
        # 而且就算用 Counter 排除 0 残留也会导致时间复杂度过高
        # 应该像 76 题一样维护 formed 判断已满足计数符号 或者 用一个长度为 26 的计数数组
        from collections import Counter, defaultdict
        left = 0
        window_dict = defaultdict(int)
        result_list = []
        need_dict = Counter(p)
        formed = 0 # 维护满足变量

        for right in range(len(s)):
            # 更新窗口字典)(增)
            window_dict[s[right]] += 1
            # 子串的长度始终都会等于 p 的长度，这是比较关键的
            # 正因为长度始终一致，不可能出现溢出的情况，因此无需对溢出进行判定，只要判定是否满足就行
            window_length = right - left + 1

            # 满足变量增加判定放在扩张后，收缩前，因为它本来就和收缩过程无关
            if s[right] in need_dict and window_dict[s[right]] == need_dict[s[right]]:
                formed += 1

            while window_length > len(p):
                # 满足变量减少判定放在收缩循环中，每次收缩前，是因为要使用旧的(将被排除的) left 来进行判定
                if s[left] in need_dict and window_dict[s[left]] == need_dict[s[left]]:
                    formed -= 1

                # 更新窗口字典 (删)
                window_dict[s[left]] -= 1

                left += 1
                window_length -= 1

            # 收缩后子串与目标字符串长度相等且满足变量达标，此时必为异位词
            if formed == len(need_dict): # need_dict 本身就是去重的，无需引入集合
                result_list.append(left)

        return result_list

sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))