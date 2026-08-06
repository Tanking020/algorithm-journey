"""
小和问题:在一个数组中,每一个数左边比其小的数之和累加起来,称为这个数组的"小和"

常规遍历算法时间复杂度:O(N^2)
此处使用归并排序算法进行简化后时间复杂度:O(NlogN)
但由于未执行预分配而是用了.append,未完美实现空间复杂度:O(N)

预分配 + 边界索引的归并算法见 px_guibing_pre.py
"""

import random
from px_maopao import random_arr

def xiaohe_guibing_sort(arr,l,r):
    """
    拆分 + 递归 主函数

    arr:待排序数组
    l:数组左边界索引
    r:数组右边界索引

    return:None
    """
    if l == r:
        return # 单个元素天然有序，无需返回
 
    mid = l + ((r-l) >> 1) # 位运算优先级低，记得加括号

    xiaohe_guibing_sort(arr,l,mid)
    xiaohe_guibing_sort(arr,mid+1,r)
    xiaohe_guibing_merge(arr,l,mid,r) # 全部是原地修改，无需返回

def xiaohe_guibing_merge(arr,l,mid,r):
    """
    .append + 边界索引版本归并 合成用工具函数

    arr:待排序数组
    l:数组左边界索引
    r:数组右边界索引

    return:None 直接原地修改arr
    """
    help_arr = []
    p1 = l
    p2 = mid + 1
    while p1 <= mid and p2 <= r:
        if arr[p1] <= arr[p2]:
            help_arr.append(arr[p1])
            p1 += 1
        else:
            help_arr.append(arr[p2])
            p2 += 1

    while p1 <= mid:
        help_arr.append(arr[p1]) # 重点1：.append和.extend的区别(都不做类型检查但每次都要检查是否有空间,后者是将可迭代对象拆开依次放入)
        p1 += 1
    while p2 <= r:
        help_arr.append(arr[p2]) # 重点2：预分配下的索引赋值 help_arr[i] = arr[p1] 的写法会比.append 性能更好
        p2 += 1
    # 原地修改help_arr数组

    for i in range(len(help_arr)):
        arr[l+i] = help_arr[i] # 将辅助数组的值传回arr,原地修改arr
    

if __name__ == '__main__':
    arr = random_arr(10,0,100)
    print(arr)
    xiaohe_guibing_sort(arr,0,len(arr)-1) # 动态边界索引 + 只原地修改
    print(arr)