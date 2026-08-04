# 选择排序

"""
选择排序：每次选最小的放到前面

时间复杂度：O(n^2)

不稳定
"""

import random

def random_array(size = 10,low = 0,high = 100):
    renturn [random.randint(low,high) for _ in range(size)]

def process(arr,l = 0,r = 9):
    for i in range(l,r):
        