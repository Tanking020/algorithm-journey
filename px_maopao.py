# 冒泡排序

import random

def random_arr(size,low,high):
    """
    随机整数列表生成函数
    
    size:数组的元素个数
    low:随机元素的下限值
    high:随机元素的上限值

    return:一个目标参数下的随机列表
    """
    return [random.randint(low,high) for _ in range(size)]

def px_maopao(arr):
    """
    冒泡排序函数：对列表进行从小到大的冒泡排序

    时间复杂度:O(N^2)

    arr:需要排序的列表

    return:None(只原地修改列表，不返回新列表)
    """
    n = len(arr)
    for j in range(n-1):
        swapped = False # 核心：如果某一轮没有发生交换，说明已经有序，可以提前结束
        for i in range(n-1-j): # 思想：分为已排序区和待排序区，每次内层从左往右遍历把最大的元素冒泡到最右边，已排序区从right往左逐渐扩张
            if arr[i] > arr[i+1]: # 大于时候进行交换，等于时候直接略过即可
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True  
        if not swapped: # 本轮无交换 → 已有序，提前退出
            break

if __name__ == '__main__':

    arr1 = random_arr(10,0,100)
    print("冒泡排序前列表：",arr1)

    px_maopao(arr1)
    print("冒泡排序后列表：",arr1)

# 原地修改和返回新数组只能二选一 我的旧代码中犯了既原地修改又返回新数组的谬误 后改成了原地修改 
# 要返回新数组就要先建立副本 对副本做修改最后返回副本（新数组），好处是不污染原数组