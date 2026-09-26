"""
基数排序
（有两类，这里只讨论最重要的_LSD最低位优先_）

适合位数不多的非负整数排序
时间复杂度: O(D × (N + K))  D=最大位数, N=数组长度, K=基数(10)
空间复杂度: O(N + K)        每轮计数排序需输出数组 + 计数数组
稳定性: 稳定

step1: 找到最大值，确定最大位数
step2: 初始化位数变量
step3: 对当前位进行计数排序
3.1 提取当前位的数字
3.2 统计每个数字出现的次数
3.3 计算前缀和 （目的：_保持排序稳定性_）
3.4 从后向前遍历，放入正确位置
step4: 把排序结果赋值回原数组
step5: 更新位数，重复第3-4步

知识点拓展:空间复杂度回答"规模变大时内存怎么涨"，额外空间回答"现在到底多花了多少内存"。前者用于比较算法，后者用于优化代码。
"""

from bubble_sort import random_arr

def count_digits(num:int) -> int:
    """
    工具函数：根据数字返回位数
    原理：循环地板除10
    最直观，性能好，代码稍长

    只能处理非负整数（符合基数排序输入约定）

    Args:
        num:待计算位数的数字

    Returns:
        digits:输入数字的位数
    """
    if num == 0:
        return 1

    digits = 0
    while num > 0:
        num //= 10
        digits += 1

    return digits

def counting_sort_for_radix(arr,exp):
    """
    工具函数：对每一位执行的稳定计数排序函数
    使用 前缀和 + 从后向前排序 保证稳定性
    使用 预分配 + 索引赋值方法

    Args:
        arr: 排序中数组
        exp: 处理中的位数

    Returns:
        None: 通过切片赋值将排序结果写回原数组（非严格原地，需 O(N) 额外空间）额外内存占用峰值为 N + 10 个整数单元，分别对应两个辅助数组，函数运行结束后被释放
    """
    n = len(arr)
    if n <= 1:
        return
    output_arr = [0] * n # 输出数组
    counting_arr = [0] * 10 # 0 到 9 共 10 个数字

    # 1. 统计当前位置上每个元素出现的次数
    for i in range(n):
        digit = (arr[i] // exp) % 10 # 核心：利用取余（模）运算 % 10 拿到当前数字对应位数的值
        counting_arr[digit] += 1

    # 2. 计算前缀和
    for j in range(1,10):
        counting_arr[j] += counting_arr[j - 1]

    # 3. 从后向前遍历，放入正确位置（保持稳定性） ！这里是核心也是难点！

    # 两种方法（可以随时取消注释并切换使用）：

    # (1): range(n-1,-1,-1)(更底层，需要索引时用) 按索引倒序遍历
    # for k in range(n-1,-1,-1):
    #   digit = (arr[k] // exp) % 10
    #   output_arr[counting_arr[digit] - 1] = arr[k]
    #   counting_arr[digit] -= 1

    # (2): reversed(更直观，更Pythonic) 按元素倒序遍历
    for num in reversed(arr):
        digit = (num // exp) % 10 # 计算当前元素对应位数的值
        output_arr[counting_arr[digit] - 1] = num
        counting_arr[digit] -= 1

    # 4. 将结果写回原数组
    arr[:] = output_arr
    
def radix_sort(arr):
    """
    基数排序（最低位优先）

    Args:
        arr: 初始待排序数组

    Returns:
        None: 通过切片赋值将排序结果写回原数组（非严格原地，需 O(N) 额外空间）
    """
    if len(arr) <= 1:
        return
    
    max_val = max(arr)

    # 根据数字返回位数的常用方法：

    # 1. 循环除以 10 最直观 性能好 代码稍长
    # digits = count_digits(max_num)

    # 2. 转字符串计算字符串长度 简洁 有转换开销
    # digits = len(str(abs(num))) # 注意原始数字要加绝对值避免负号占位

    # 3. 直接用 位数变量 exp 进行判断 无需单独求位数 只能在基数排序中用 （这是本次代码中实际使用的方法）
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr,exp)
        exp *= 10

if __name__ == '__main__':
    arr = random_arr(10,0,100)
    print("基数排序前列表:",arr)
    radix_sort(arr)
    print("基数排序后列表:",arr)