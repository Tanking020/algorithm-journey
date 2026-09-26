"""
堆排序
时间复杂度：
1；建堆：O(N) (Floyd方法)
2；排序：O（NlogN）
最坏情况下
空间复杂度：O（1）

与归并排序及快速排序相比，优势是空间复杂度较低，缺点是不稳定

关键优势：堆排序是少数在最坏情况下仍能保证 O(N log N) 的排序算法。
快排最坏会退化到 O(N^2)，而堆排序不会。

借助完全二叉树-大根堆-摘取最大值

执行步骤:先对原数组排成一个大根堆(指针向右依次行进,执行heap_insert不断上浮到合适位置)-执行摘顶操作-对顶末交换后的新完全二叉树从上到下执行heapify-如此循环直到heap_size <= 1
注意：执行步骤第一步已从 插入上浮法 被修正为 floyd建堆法（堆排序标准做法）

逐个插入上浮法：适合动态流式数据，一个一个来
floyd方法：适合已有完整数组的情况下批量建堆

堆结构三类操作:
heap_insert:向上和父元素对比
heapify:向下和大儿子对比
摘顶:把末尾元素和顶部元素对比,同时 heap_size -= 1

错因汇总:
1.没有注意DRY原则,为了提高维护性要把下沉操作单独写成函数而不是在每个要用的地方写
2.建堆函数算法写得不够好，从正确性来说用逐个插入上浮法也对，但是建堆复杂度是O（NlogN）,若用Floyd方法，建堆复杂度仅O（N）

一个底层逻辑:扩容（成倍&逐个）
一个重要定义:黑盒：系统中封装好的标准库，例如python中的heapq，其支持建堆，插入，摘顶的操作，但是不支持改，不支持删中间，需要后面两类操作就要手写堆
黑盒名字由来：因为只能看到它的对外接口，看不到它的内部实现细节
"""

import random

from bubble_sort import random_arr
from merge_sort import merge_sort

def heap_insert(arr):
    """
    工具函数:使用逐个插入上浮法将数组排成一个大根堆
    建堆复杂度：O(NlogN)(不够好，已替换为floyd方法)

    Args:
        arr:待建堆数组

    Returns:
        None(原地修改)
    """
    if len(arr) <= 1:
        return
    
    for j in range(1,len(arr)):
        i = j
        while i > 0 and arr[i] > arr[(i-1)//2]:
            arr[i],arr[(i-1)//2] = arr[(i-1)//2],arr[i]
            i = (i-1)//2 # 使用 for 循环遍历数组元素，嵌套 while 条件循环对每个遍历到的元素执行不断交换上浮直到满足条件的操作

def heap_floyd(arr):
    """
    工具函数:使用floyd方法将数组排成一个大根堆
    建堆复杂度：O(N)
    这是堆排序的巨大优势所在，堆排序必须使用floyd方法自下而上建堆

    Floyd建堆法核心思维：不是"构建"，而是"修复"

    【视角转换】从"空堆生长"到"满树修复"
        - 插入上浮法视角：堆一开始是空的，数据是一个个"外来者"，需要被"安插"到正确位置
        - Floyd法视角：数组本身就已经是一棵结构完美的完全二叉树了，
          只是节点上的值不满足堆序性质。我们不需要改变树的形状，只需要把值"调整"到位

      【自底向上的"信任传递"】为什么必须从下往上、从右往左？
        前提：对某个节点执行 heapify（下沉）时，其左右子树必须已经是合法的堆
        保证：自底向上遍历确保处理第 i 层时，第 i+1 层及以下所有子树都已被修复为合法堆
        效果：一次 heapify 就能把当前节点为根的子树也变成合法堆，
              像多米诺骨牌一样把"合法性"向上传递，直到根节点
     
      【O(N) 复杂度直觉】
        Floyd法之所以快，是因为绝大多数节点都在底层，而底层节点几乎不需要移动；
        需要长距离移动的顶层节点又极其稀少。两者完美对冲

    Args:
        arr:待建堆数组
    
    Returns:
        None(原地修改)
    """
    n = len(arr)
    for i in range(n//2 - 1,-1,-1): # 从下往上，从右往左第一个非叶子节点开始计算，省去对大量叶子节点的操作（叶子节点没有孩子，天然满足大根堆定义）
        heap_heapify(arr,i,n)

def heap_heapify(arr,index,heap_size):
    """
    工具函数:执行单次heapify操作

    Args:
        arr:待排序数组(排序中)
        index:当前待下沉(heapify)元素的索引
        heap_size:当前大根堆中的节点个数
    
    Returns:
        None(原地修改)
    """
    while 2*index + 1 < heap_size: # 与其用 <= 加 减号 不如直接用 < ，规避掉一个不必要的减法运算

        # if 2 * index + 2 >= heap_size: # 避免在arr[right]不存在的时候错误地进行索引 但是每次都要先单独执行右孩子存在性判别（缺陷）
        #     largest = 2 * index + 1
        # elif arr[2 * index + 1] > arr[2 * index + 2]:
        #     largest = 2 * index + 1
        # else:
        #     largest = 2 * index + 2

        # if arr[index] < arr[largest]:
        #     arr[index],arr[largest] = arr[largest],arr[index]
        # else:
        #     break

        # 优化：使用另一种模式（_挑战者模式(或擂台赛)_，依次挑战），避免嵌套分支（上面注释掉的这种）利用到了if条件语句判定前者条件不满足直接结束而不会再判断右边条件的性质，避免了在arr[right]不存在的时候错误地进行索引
        
        left = 2 * index + 1 # 避免多次进行不必要的乘法运算 
        right = 2 * index + 2
        max_idx = index

        if left < heap_size and arr[left] > arr[max_idx]: # 不再先对左右孩子进行判别大小，而是先与左孩子比大小判max_idx再用新的max_idx与右孩子（若存在）比大小判max_idx 
            max_idx = left
        if right < heap_size and arr[right] > arr[max_idx]:
            max_idx = right

        if max_idx == index:
            break

        arr[index], arr[max_idx] = arr[max_idx], arr[index] # 逗号后加空格， * 号左右都加空格，能提高可读性
        index = max_idx

def heap_sort(arr):
    """
    堆排序对外端口

    依赖工具函数：
    heap_insert(arr) -> 优化后改为: heap_floyd
(arr)
    heap_heapify(arr,index,heap_size)

    Args:
        arr:待排序数组(用户输入的初始数组)
        
    Returns:
        None(原地修改)
    """

    if len(arr) <= 1:
        return

    heap_size = len(arr)
    # heap_insert(arr) - 优化为floyd建堆
    heap_floyd(arr)

    while heap_size > 1:
        arr[heap_size - 1],arr[0] = arr[0],arr[heap_size - 1] # 注意，排序循环不要每次都重复建堆，把末尾交换上去直接向下条件循环执行heapify
        heap_size -= 1
        heap_heapify(arr,0,heap_size) # 传入参数 index=0 不变，那就直接传入0就可以，避免产生变量名混淆影响维护性

def heap_test(size,low,high):
    """
    堆排序结果测试函数:
    测试工具:预处理-归并排序函数
    """
    arr = random_arr(size,low,high)
    print("堆排序前的指定参数随机数组:",arr)
    arr2 = arr.copy()
    heap_sort(arr)
    print("指定随机整数数组arr堆排序后:",arr)
    merge_sort(arr2)
    print("指定随机整数数组arr创建副本并对副本预处理-归并排序后:",arr2)
    print("经预处理-归并排序检验:")
    print("堆排序结果与归并排序核验一致!" if arr == arr2 else "堆排序结果与归并排序核验不一致!请校检代码!")

if __name__ == '__main__':
    heap_test(100,0,100)