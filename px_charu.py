# 插入排序

import random

def random_arr(size,low,high):
    """
    随机整数列表生成函数

    size:列表元素个数
    low:元素生成范围(下)
    high:元素生成范围(上)
    
    return:一个给定参数下生成的随机整数列表
    """
    return [random.randint(low,high) for _ in range(size)]

def px_charu(arr):
    """
    插入排序算法
    把新元素插入到_已排序区_的合适位置
    注意插入和交换的区别:插入后已排序区右侧元素要整体往后挪一位(借助while条件循环实现)

    arr:待排序列表
    return:None(原地修改)
    """
    n = len(arr)
    for i in range(1,n): # 注意遍历范围,由于后续要用到i-1,这里i不能从0开始
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j] # 也就是说：从第i元素（key）往左逐个看谁比key大，把比key大的往右挪一格
            j -= 1 # 在每个i的讨论中while遍历其左侧所有元素（事实上 j -= 1 是while循环经典操作，注意理解即可）
            # 最后j到达已排序区边界时内层循环结束
        arr[j+1] = key # while 结束后，j+1 就是 key 的正确插入位置

if __name__ == '__main__':
    arr = random_arr(10,0,100)
    print("插入排序前列表：",arr)
    px_charu(arr)
    print("插入排序后列表",arr)
