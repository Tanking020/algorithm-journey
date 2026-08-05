"""
小和问题:在一个数组中,每一个数左边比其小的数之和累加起来,称为这个数组的"小和"

常规遍历算法时间复杂度:O(N^2)
此处使用归并排序算法进行简化后时间复杂度:O(NlogN)
空间复杂度:O(N)
"""

import random
from px_maopao import random_arr

def xiaohe_guibing_sort(arr,l,r,help_arr):
    if l == r:
        return # 单个元素天然有序，无需返回
 
    mid = l + ((r-l) >> 1) # 位运算优先级低，记得加括号

    xiaohe_guibing_sort(arr,l,mid,help_arr)
    xiaohe_guibing_sort(arr,mid+1,r,help_arr)
    xiaohe_guibing_merge(arr,l,mid,r,help_arr) # 全部是原地修改，无需返回

def xiaohe_guibing_merge(arr,l,mid,r,help_arr):
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
        help_arr.append(arr[p1]) # 重点1：.append和.extend的区别
        p1 += 1
    while p2 <= r:
        help_arr.append(arr[p2]) # 重点2：预分配下的索引赋值 hepl_arr[i] = arr[p1] 的写法会比.append 性能更好
        p2 += 1
    # 只原地修改数组，这里依然无需写返回

if __name__ == '__main__':
    arr = random_arr(10,0,100)
    print(arr)
    help_arr = []
    arr2 = xiaohe_guibing_sort(arr,0,9,help_arr)
    print(help_arr)