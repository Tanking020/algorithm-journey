"""
(伪)归并排序算法(len + 切片版)——分治思想,先拆后合
    核心关键点:
        1:递归的 base case (递归的终止条件) 是len(arr) <= 1,当然也可以用l(左边界索引)==r(右边界索引)
        2:合并时用双指针
        3:需要额外的临时数组(返回新数组而不是原地修改)

空间复杂度更低的"真·归并排序算法"可参考merge_sort.py
"""

import random

def random_arr_float(size,low,high,ndigits):
    """
    随机浮点数列表生成函数

    size:元素个数
    low:元素下界
    high:元素上界
    ndigits:保留多少位小数(不是python内定参数,改成别的英文也行)

    return:一个符合参数要求的随机浮点数列表
    """
    return [round(random.uniform(low,high),ndigits) for _ in range(size)] # 利用round(number,ndigits)函数_对数字进行四舍五入，保留指定的小数位数_

def merge_sort_naive(arr):
    """
    (伪)归并排序算法(len + 切片版)：递归拆分和排序将数组递归拆分为最小单元(子问题),再通过px_guibing_merge(也就是下面的合并函数)逐层合并为有序数组
    时间复杂度:O(nlogn) _没有浪费比较行为_
    原算法额外空间复杂度:O(N) _空间换时间_ 每次申请空间后又释放掉了,最多只需要申请一个长度为N的空间
    在本文档中为方便理解使用了基于长度(len,而非边界索引l与r)+切片(切片操作必定产生新列表而非原地修改)的方法,实际额外空间复杂度:O(NlogN)
    稳定

    arr:待归并排序的列表
    
    return:排好序的新列表（不修改原数组）
    """
    if len(arr) <= 1: #<=1中的=0是一种_防御性编程_。正常流程不会触发它，但万一有人传了空数组进来，代码也不会崩。
        return arr
    
    mid = len(arr)//2
    left = merge_sort_naive(arr[:mid])
    right = merge_sort_naive(arr[mid:]) # 创建新数组而不是原地修改,导致空间复杂度上升到O(NlogN)

    return merge_naive(left,right)

def merge_naive(left,right):
    """
    合并函数:给归并排序函数用的工具函数,无需由用户主动调用

    left:左侧有序数组
    right:右侧有序数组

    return:合并后的有序新数组
    """
    result = [] # 创建新数组用于存放合并结果
    i = j = 0 # i 指向left当前元素;j指向right当前元素(_双指针操作_)

    while i < len(left) and j < len(right): # 注意这里只能小于不能等于，列表索引是从0开始的，当等号成立时i就越界了
        if left[i] <= right[j]:
            result.append(left[i]) # 比较双指针对应元素大小，将更小的添加进result，并且确定当两元素相等时优先传输left列表中的元素
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 拼接剩余:拼接还有残余的那个有序子数组
    # 残余有序子数组中的元素一定比已添加的所有元素都大或一样大

    result.extend(left[i:])
    result.extend(right[j:])

    return result

if __name__ == '__main__':
    arr = random_arr_float(10,0.0,100.0,2)
    print("归并排序前的列表:",arr)
    result = merge_sort_naive(arr)
    print("归并排序后的列表:",result)