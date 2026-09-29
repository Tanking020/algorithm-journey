class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 解法：栈（属于配对/抵消栈）
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        pairs = {'}': '{', ']': '[', ')': '('}
        st = []

        # for char in s:
        #     st.append(char)
        #     # 注意：条件判断符号有优先级 not > and > or 因此最外层必须加括号避免 len 判定只保护第一个分支
        #     # while len(st) >= 2 and (
        #     #     (st[-1] == '}' and st[-2] == '{') 
        #     #     or (st[-1] == ']' and st[-2] == '[') 
        #     #     or (st[-1] == ')' and st[-2] == '(')):
        #     # 更精简的写法：使用映射表替代一长串布尔表达式
        #     while len(st) >= 2 and st[-2] == pairs.get(st[-1]): # 用.get()安全取某个键的值，不指定默认值时返回 None
        #         st.pop();st.pop() # 两次.pop()操作按对删除

        # 上面代码已经达成时空复杂度要求，这里是一种基于提前终止的常数优化写法：
        for char in s:
            if char in pairs:
                # 情形一：遇到右括号时栈已为空，说明没有可配对的左括号，永远无法正确匹配
                # 情形二：出栈的元素不是 char 对应的左括号，说明括号发生了交叉嵌套，同样无法正确匹配
                # 在这两种情形下可以直接返回
                # .pop() 放在条件判断中时候会删除并返回被删除元素拿来判断
                # 但是这里发生了短路求值，not st放在前面会导致 当st为空时候.pop()不会被执行
                if not st or st.pop() != pairs[char]: 
                    return False

            else:
                st.append(char)

        return not st
    
sol = Solution()
print(sol.isValid("()[]{}"))
