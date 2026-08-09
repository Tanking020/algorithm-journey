# 选择排序

import random
from bubble_sort import random_arr

def selection_sort(arr):
    """
    选择排序：每次从待排序区选最小的，放到已排序区末尾（交换）。
    时间复杂度:O(n^2)
    不稳定
    和冒泡的区别：冒泡是“交换相邻的”，选择是“找到最小的再交换”
    选择排序的交换次数最少（最多 n-1 次）

    arr:待排序列表

    return:None(原地修改)
    """
    n = len(arr)
    for i in range(n-1):# 优化：外层循环可以少跑一轮当 i == n-1 时，待排序区只剩最后一个元素，它必然是最小的，无需再比较和交换
        min_index = i
        for j in range(i,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

if __name__ == '__main__':
    arr = random_arr(10,0,100)
    print("选择排序前列表:",arr)
    selection_sort(arr)
    print("选择排序后列表:",arr)