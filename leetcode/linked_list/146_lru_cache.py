class LRUCache(object):

    def __init__(self, capacity):
        # 解法：
        # 时间复杂度：
        # 空间复杂度：
        pass

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        pass

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        pass


# —— 本地自测 ——
# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))       # 1
# cache.put(3, 3)           # 淘汰 key 2
# print(cache.get(2))       # -1
# print(cache.get(3))       # 3
