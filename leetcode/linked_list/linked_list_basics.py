class Node(object):
    """
    定义节点类
    """
    # 类声明：object 是父类（只有基础功能），类似的还有 list 等子类（自带.append()等）
    def __init__(self, data):
        """
        初始化节点
        """
        self.data = data # 数据域：存储数据
        self.next = None # 指针域：初始化为 None, 表示不指向任何节点

class LinkedList(object):
    """
    定义单向链表类

    声明：存在许多 print 操作，仅为练习直观展示，实际使用时候不写
    """
    def __init__(self):
        """
        初始化链表，头指针指向 None
        """
        self.head = None # 头指针，初始化为 None 表示空链表
        self.size = 0 # 链表长度，方便获取长度（可选优化）

    def is_empty(self):
        """
        判断链表是否为空
        """
        # is None 判对象，== 判值，判 None 用 is 更快且不受 __eq__ 干扰，其余比值用 ==
        # None、各种零、各种空容器 判 False, "0"、""、-1、[0] 都判 True
        return self.head is None

    def __len__(self):
        """
        获取链表长度
        """
        return self.size

    def __str__(self):
        """
        打印链表内容
        """
        # 用写过的判空方法来做判空
        if self.is_empty():
            return "空链表"

        result = []
        current = self.head

        # 从头节点开始遍历并添加到列表末尾
        while current is not None:
            result.append(str(current.data))
            current = current.next

        # 用 " -> " 连接所有数据，最后加上 None 表示链表结束
        # 语法：胶水.join(一串字符串)  胶水在前，只加在中间；元素必须都是字符串；返回新字符串
        # 右边括号内不一定是列表，任何可迭代对象都行，但是其元素必须都是字符串
        # 小注意点：字符串中空格有意义不要乱打空格
        return  " ->".join(result) + " -> None"

    def insert_at_head(self, data):
        """
        头插法：在链表头部插入新节点

        时间复杂度：O(1)
        """
        # 创建新节点
        new_node = Node(data)

        # 将新节点的 next 指向原来的头节点
        new_node.next = self.head

        # 更新头指针，让头指针指向新节点
        # 换头，而不是 self.head.next
        self.head = new_node

        # 链表长度更新
        self.size += 1

        print(f"头插法插入 {data} 成功")

    def insert_at_tail(self, data):
        """
        尾插法：在链表尾部插入新节点
        时间复杂度：O(n)

        ! 待优化：再维护一个 self.tail 指针，尾插就能 O(1)
        """
        # 创建新节点
        new_node = Node(data)

        # 链表判空
        # 空链表头指针指向 None, 此时新节点直接成为头节点就是插入新节点了
        if self.is_empty():
            self.head = new_node
            self.size += 1 # 顺手更新链表长度，后面不再注释
            print(f"尾插法插入 {data} 成功（链表原本为空）")
            return

        # 遍历链表，找到最后一个节点
        current = self.head
        # 跳出循环时就是最后一个节点（指向 None）
        while current.next is not None:
            current = current.next

        # 让最后一个节点的 next 指向新节点
        # 新节点自动指向默认值 None
        current.next = new_node

        self.size += 1
        print(f"尾插法插入 {data} 成功")

    def insert_at_position(self, position, data):
        """
        指定位置插入：在第 position 个位置（从 1 开始）插入新节点
        """
        # 检查位置是否合法
        # "->(head) node1 -> position = 1 -> node2 -> None"
        if position < 1 or position > self.size + 1:
            print(f"插入位置无效")
            return

        # 如果插入位置是头部，直接使用头插法
        if position == 1:
            self.insert_at_head(data)
            return

        # 创建新节点
        new_node = Node(data)

        # 遍历到 position - 1 的位置
        current = self.head
        # 利用序号变量维护控制位置
        current_pos = 1

        # 跳出循环时 current_pos = position
        while current_pos < position:
            current = current.next
            current_pos += 1

        # 插入操作（依旧是先存住链表尾部防丢失）：新节点的 next 指向 current 的下一个节点
        new_node.next = current.next
        # current 的 next 指向新节点
        current.next = new_node

        self.size += 1
        print(f"在位置 {position} 插入 {data} 成功")

    def delete_by_value(self, value):
        """
        按值删除：删除第一个值为 value 的节点
        """
        # 链表为空时候直接返回
        if self.is_empty():
            print("链表为空，无法删除哦")
            # 返回布尔变量以后可以检查删除成功了没
            return False

        # 如果要删除的是头节点：
        if self.head.data == value:
            # 头指针指向下一个节点（python 中自动释放了原本的头节点）
            self.head = self.head.next
            self.size -= 1
            print("头节点删除成功")
            return True

        # 遍历链表，找到要删除的节点的前一个节点
        current = self.head

        # 用 != value 判定是否到达目标值，用 is not None 避免越界
        while current.next is not None and current.next.data != value:
            current = current.next

        # 如果 current.next == None, 说明没找到（链表中不存在）
        if current.next is None:
            print(f"未找到值为 {value} 的节点！")
            return False

        # 执行删除操作：current 的 next 直接跳过要删除的节点（简洁）
        current.next = current.next.next
        self.size -= 1
        print(f"删除值为 {value} 的节点成功！")
        return True

    def delete_at_position(self, position):
        """"
        按位置删除：删除第 position 个节点（从 1 开始）
        """
        # 检查位置是否合法