class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 错误旧思路：仅仅对strs数组执行了异位词聚拢，但没有分组装成列表
        # n = len(strs)
        # if n <= 1:
        #     return
        # i = 0
        # while i in range(n):
        #     for k in range(i+1,n):
        #         if sorted(strs[i]) == sorted(strs[k]):
        #             strs[i+1], strs[k] = strs[k], strs[i+1]
        #             i += 1
        #     i += 1

        # 以下是正确思路：
        result = {} # 创建字典 利用键值对去做这个题

        for i in strs:
            key = tuple(sorted(i)) # 对字符串进行排序，排序后转化为元组作为哈希表（字典）中该字符串对应的键（分类）
                                   # 不使用列表作为键是因为列表不可哈希，所以不能做字典的键。元组可哈希，所以能做。
            if key not in result:
                result[key] = [] # 出现未见过的键（分组）时候建立一个新的空列表作为新键的值

            result[key].append(i) # 在对应的键的值列表把这个字符串加入到末尾

        return list(result.values()) # 把字典中所有值（也就是所有分组好后的列表）取出来，组成列表后返回

# 测试
sol = Solution()
print(sol.groupAnagrams(["eat","tan","ate","ant","ui","eta"]))