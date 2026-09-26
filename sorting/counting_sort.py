"""
计数排序 .extend版本

使用计数加一然后按次数放回的标准实现，不稳定

可优化为：预分配+索引赋值 还有就是可以用前缀和 + 从后向前遍历的写法，使排序具有稳定性

计数排序就是桶大小为 1 的桶排序

此模块中的对数器写得比较完善，可以作为以后写对数器的参考
"""

import random
from bubble_sort import random_arr
from merge_sort import merge_sort

def counting_sort(arr,min_val,max_val):
    """
    计数排序

    Args:
        arr:待计数排序数组
        min_val:待排序数组中元素最小值(允许比实际最小值更小但不可更大)
        max_val:待排序数组中元素最大值(允许比实际最大值更大但不可更小)

    Returns:
        None:仅原地修改传入数组，过程中使用计数数组和结果数组作为辅助空间，函数返回后自动释放
    """

    if not arr: # 对空数组进行防御
        return
    count_arr = [0] * (max_val - min_val + 1)

    for i in range(len(arr)):
        count_arr[arr[i] - min_val] += 1 # 计数数组 = 类似频域空间 一定要注意计算偏移量

    result_arr = []

    j = 0
    n = len(count_arr)
    while j < n:
        if count_arr[j] == 0:
            j += 1
            continue
        else:
            result_arr.extend([j + min_val] * (count_arr[j])) # .extend思路不错，但是改成预分配思想会更好
            j += 1

    for k in range(len(result_arr)):
        arr[k] = result_arr[k]

def counting_sort_test(min_val,max_val,low,high,test_times):
    """
    测试函数:利用归并排序检验手写的计数排序的正确性

    Args:
        min_val:随机生成数组中元素个数可能的最少值
        max_val:随机生成数组中元素个数可能的最多值
        low:随机生成的待排序数组中元素可能的最小值
        high:随机生成的待排序数组中元素可能的最大值
        test_times:测试次数

    Returns:
        bool:测试结果 打印测试结果，将不一致结果及其测试序号给出
    """

    test_result = True
    for i in range(test_times): # 用 for 循环便于维护
        size = random.randint(min_val,max_val) # 使用随机尺寸数组生成，便于检查各类情形
        arr = random_arr(size,low,high)

        arr_original = arr.copy() # 保留原始数组
        arr_test = arr.copy()
        
        counting_sort(arr,low,high)
        
        merge_sort(arr_test)

        if arr != arr_test:
            test_result = False
            print(f"在第{i}次检验中两类排序结果不一致:原始数组:{arr_original} \n 计数:{arr} \n 归并:{arr_test}") # 保留原始数组便于检查问题
            break

    print(f"所有{test_times}次校验全部通过!" if test_result == True else "校验未通过!请检查代码漏洞!")
    return test_result # 根据测试结果返回测试通过与否，便于后续其他引用

if __name__ == '__main__':
    counting_sort_test(0,100,0,100,1000) # 测试时候要把小尺寸包含进去，特别是 数组长度为 0 这个边界处最容易出问题