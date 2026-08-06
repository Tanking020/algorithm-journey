"""
小和问题:在一个数组中,每一个数左边比其小的数之和累加起来,称为这个数组的"小和"

常规遍历算法时间复杂度:O(N^2)
此处使用归并排序算法进行简化后时间复杂度:O(NlogN)
但由于未执行预分配而是用了.append(需要检查内存) + 每次 merge 都新建 help_arr
峰值空间复杂度仍为O(N)，但因频繁创建/销毁临时数组，常数开销较大

注意,为了不修改原始数组,将不采用原地修改的写法,而是传入原数组的副本

预分配 + 边界索引的归并算法见 px_guibing_pre.py
"""

import random
from px_maopao import random_arr

def xiaohe(arr):
    """
    对外接口:返回数组的小和

    arr:待求解小和的数组

    return:传入数组的小和计算结果
    """

    if not arr or len(arr) <= 1:
        return 0 # 边界条件处理:此时小和显然为0

    # 传入副本,_避免修改调用者的原始数组
    return xiaohe_guibing_sort(arr.copy(),0,len(arr)-1) # 这里.copy的操作需要加深理解！！！ .copy() 创建浅拷贝，确保归并排序的原地修改不会污染调用者的原始数组

def xiaohe_guibing_sort(arr,l,r):
    """
    拆分 + 递归 主函数
    返回当前区间内产生的小和

    arr:待排序数组
    l:数组左边界索引
    r:数组右边界索引

    return:当前区间内产生的小和
    """
    if l == r:
        return 0 # 单个元素数组自身的小和为0
 
    mid = l + ((r-l) >> 1) # 位运算优先级低，记得加括号

    left_sum = xiaohe_guibing_sort(arr,l,mid)
    right_sum = xiaohe_guibing_sort(arr,mid+1,r)
    cross_sum = xiaohe_guibing_merge(arr,l,mid,r) # 三处可能产生小和的比较场景 (新数组包含的小和 = 左子数组包含的 + 右子数组包含的 + 左右子数组合并时产生的)

    return left_sum + right_sum + cross_sum

def xiaohe_guibing_merge(arr,l,mid,r):
    """
    .append + 边界索引版本归并 合成用工具函数
    版本归并 + 小和累加

    arr:待排序数组
    l:数组左边界索引
    r:数组右边界索引

    return:本次合并中跨越左右两半产生的小和
    """
    help_arr = []
    p1 = l
    p2 = mid + 1
    cross_sum = 0

    # 原地修改 help_arr 数组
    while p1 <= mid and p2 <= r:
        if arr[p1] < arr[p2]: # 为符合小和定义,这里只能严格小于号
            help_arr.append(arr[p1])
            cross_sum += arr[p1] * (r - p2 + 1) # 简化思路:由于两子数组各自都是从小到大有序的,所以当发生严格小于,后面的所有数也就不用比了,可以直接计算该左元素对应小和计算次数
            p1 += 1
        else:
            help_arr.append(arr[p2]) # 需要注意的是,在小和问题求解中,左右指针对应元素相等时,应该总是让右边指针推进,否则无法准确知道左边每个指针对应的小和了(还没比完该左元素就被跳过了)
            p2 += 1

    while p1 <= mid:
        # 此时左侧子数组有剩余.表明这些一定比右侧已排序区元素都大(或者等于),自然也不也就是说此时有待计算计入小和次数的元素,但是它们的计入次数都是0
        help_arr.append(arr[p1]) # 重点1：.append和.extend的区别(都不做类型检查但每次都要检查是否有空间,后者是将可迭代对象拆开依次放入)
        p1 += 1
    while p2 <= r:
        # 此时右侧子数组有剩余,但要计算的是左侧元素在小和的计入次数,因此这个情形下不会有新的待计算计入小和次数的元素,cross_sum不会再增加
        help_arr.append(arr[p2]) # 重点2：预分配下的索引赋值 help_arr[i] = arr[p1] 的写法会比.append 性能更好
        p2 += 1 

    for i in range(len(help_arr)):
        arr[l+i] = help_arr[i] # 将排好序的 help_arr 回写到 arr 的 [l, r] 区间

    return cross_sum
    
if __name__ == '__main__':
    arr = random_arr(10,0,100)
    print("待进行小和计算的数组:",arr)

    # 用遍历算法检验结果的正确性:
    brute = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                brute += arr[j]

    """
    # 一种更高级的写法:

    brute = sum(
        arr[j]
        for i in range(len(arr))
        for j in range(i)
        if arr[j] < arr[i])

    # 这里不需要写缩进是因为sum的参数是一个表达式而非语句代码块 同样的原因无需打冒号
    """

    result = xiaohe(arr)
    print("传入数组小和计算的结果:",result)

    print(f"检验原数组是否被污染:{arr},若和传入数组一致均未有序,说明最终未修改原数组而是严格执行了.copy副本传入")

    print(f"遍历算法暴力求解下的小和真值:{brute}")
    print(f"校验通过!" if brute == result else f"校验失败!差值:{result - brute}")