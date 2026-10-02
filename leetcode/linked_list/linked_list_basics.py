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
        # 类型注解：next 既可以是一个节点，也可以是 None（表示后面没有节点了）
        # 不加注解时 Pylance 会把 next 推断成"永远是 None"，后面所有赋值/访问都会报错
        self.next: "Node | None" = None # 指针域：初始化为 None, 表示不指向任何节点

class LinkedList(object):
    """
    定义单向链表类

    声明：存在许多 print 操作，仅为练习直观展示，实际使用时候不写而是只用布尔变量返回法
    """
    def __init__(self):
        """
        初始化链表，头指针指向 None
        """
        # 类型注解：head 可以指向一个节点，也可以是 None（空链表）
        self.head: "Node | None" = None # 头指针，初始化为 None 表示空链表
        self.size = 0 # 链表长度，方便获取长度（可选优化）

    def is_empty(self) -> bool:
        """
        判断链表是否为空

        返回:
            链表是否为空
        """
        # is None 判对象，== 判值，判 None 用 is 更快且不受 __eq__ 干扰，其余比值用 ==
        # None、各种零、各种空容器 判 False, "0"、""、-1、[0] 都判 True
        return self.head is None

    def __len__(self) -> int:
        """
        获取链表长度

        返回：
            链表长度
        """
        return self.size

    def __str__(self) -> str:
        """
        打印链表内容

        返回：
            包含 " -> " 的链表打印结果字符串
        """
        # 这里不用 self.is_empty()：直接判 self.head，
        # 这样 Pylance 能把 head 的类型从 "Node | None" 收窄成 "Node"（is_empty() 做不到）
        if self.head is None:
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
        return " -> ".join(result) + " -> None"

    def insert_at_head(self, data) -> bool:
        """
        头插法：在链表头部插入新节点

        时间复杂度：O(1)

        返回：
            插入操作是否顺利完成
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
        return True

    def insert_at_tail(self, data) -> bool:
        """
        尾插法：在链表尾部插入新节点
        时间复杂度：O(n)

        ! 待优化：再维护一个 self.tail 指针，尾插就能 O(1)
        """
        # 创建新节点
        new_node = Node(data)

        # 链表判空
        # 空链表头指针指向 None, 此时新节点直接成为头节点就是插入新节点了
        # 直接判 self.head（不用 self.is_empty()）→ 后面 Pylance 就知道 current 不可能是 None
        if self.head is None:
            self.head = new_node
            self.size += 1 # 顺手更新链表长度，后面不再注释
            print(f"尾插法插入 {data} 成功（链表原本为空）")
            return True

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
        return True

    def insert_at_position(self, position, data) -> bool:
        """
        指定位置插入：在第 position 个位置（从 1 开始）插入新节点
        """
        # 检查位置是否合法
        # "->(head) node1 (-> position = 2) -> node2 -> None"
        if position < 1 or position > self.size + 1:
            print(f"插入位置无效")
            return False

        # 如果插入位置是头部，直接使用头插法
        if position == 1:
            self.insert_at_head(data)
            return True

        # 创建新节点
        new_node = Node(data)

        # 走到这里说明 position >= 2 → 链表至少有 1 个节点 → head 必然不为 None
        # assert 就是把"我们知道、但类型检查器不知道"的事告诉 Pylance 的标准做法
        assert self.head is not None

        # 遍历到 position - 1 的位置
        current = self.head
        # 利用序号变量维护控制位置
        current_pos = 1

        # 跳出循环时 current_pos = position - 1
        # 条件里带上 current is not None，Pylance 才能确定循环体里 current 不是 None
        while current is not None and current_pos < position - 1:
            current = current.next
            current_pos += 1

        # position 已校验 → 前驱节点必然存在
        assert current is not None

        # 插入操作（依旧是先存住链表尾部防丢失）：新节点的 next 指向 current 的下一个节点
        new_node.next = current.next
        # current 的 next 指向新节点
        current.next = new_node

        self.size += 1
        print(f"在位置 {position} 插入 {data} 成功")
        return True

    def delete_by_value(self, value) -> bool:
        """
        按值删除：删除第一个值为 value 的节点
        """
        # 链表为空时候直接返回（直接判 head，便于后面 Pylance 收窄类型）
        if self.head is None:
            print("链表为空，无法删除哦")
            # 返回布尔变量以后可以检查删除成功了没
            return False

        # 如果要删除的是头节点：
        # 需要特判是因为头节点没有前驱，没法用"跳过"那一招
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

        # 执行删除操作：current 的 next 直接"跳过"要删除的节点（简洁）
        current.next = current.next.next
        self.size -= 1
        print(f"删除值为 {value} 的节点成功！")
        return True

    def delete_at_position(self, position) -> float | None:
        """
        按位置删除：删除第 position 个节点（从 1 开始）

        返回：
            被删除的值
        """
        # 检查位置是否合法
        if position < 1 or position > self.size:
            print("删除位置不合法")
            return None

        # 位置合法 → 1 <= position <= size → 链表至少有 1 个节点 → head 必然不为 None
        assert self.head is not None

        # 如果要删除的是头节点
        if position == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            self.size -= 1
            print(f"删除位置 1 （数据 {deleted_data}） 成功")
            # 删除操作返回被删除的值
            return deleted_data

        # 遍历到删除位置的前一个节点
        current = self.head
        current_pos = 1

        # 删除操作和插入操作中"位置"的意义有区别
        while current is not None and current_pos < position - 1:
            current = current.next
            current_pos += 1

        assert current is not None

        # 保存被删节点：position 已校验 → 目标节点必然存在
        target = current.next
        assert target is not None
        deleted_data = target.data

        # 删除操作：跳过要删除的节点
        current.next = target.next
        self.size -= 1

        print(f"删除位置 {position} 位置数据 {deleted_data} 成功")
        return deleted_data

    # 从此处开始不写 print, 仅用返回值代表含义
    def search(self, value) -> int:
        """
        按值查找：查找第一个值为 value 的节点
        """
        current = self.head
        position = 1

        # 遍历建立：不要漏掉头节点的判定哦
        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position += 1

        # 除了 None 也可以用合法类型里的一个特殊值（如 -1）表示失败
        # 也是 int 类型但必须在真实数据域之外
        return -1

    def get_at_position(self, position) -> None | float:
        """
        按位置获取：获取第 position 个节点的数据
        """
        # 检查位置是否合法
        if position < 1 or position > self.size:
            return None

        # 位置合法 → 链表至少有 1 个节点 → head 必然不为 None
        assert self.head is not None

        current = self.head
        current_pos = 1

        # 同上：条件里带上 current is not None，帮助 Pylance 收窄
        while current is not None and current_pos < position:
            current = current.next
            current_pos += 1

        # position 已校验 → 第 position 个节点必然存在
        assert current is not None

        return current.data

    def reverse(self) -> bool:
        """
        反转链表：将链表顺序颠倒

        时间复杂度：O(n)
        """
        # 自画思路图：
        # "->(.head) node1(cur) -> node2 -> node3 -> node4 -> node5 -> None"
        # "None == prev <- node1(cur) | next_node -> node2 -> node3 -> node4 -> node5 -> None"
        # "None <- node1  == next_node(cur) | -> node2 -> node3 -> node4 -> node5 -> None"
        # "None <- node1 == prev <- node2(cur) <-(.head) | next_node -> node3-> node4-> node5 -> None"
        # ...
        # "None <- node1 <- node2 <- node3 <- node4 <- node5 <-(.head)"

        # 先判空 / 只有一个节点
        # 直接判 self.head（不用 self.is_empty()）→ 通过后 Pylance 知道 head 必为 Node
        if self.head is None or self.head.next is None:
            return True

        # 前一个节点，初始为 None
        prev = None

        # 当前节点，从头开始
        current = self.head

        # 遍历链表，逐个指针反转方向，头指针不参与逐节点反转，循环结束后统一赋值 self.head = prev
        while current is not None:
            # 先保存下一个节点，防止断链
            next_node = current.next
            # 当前节点指向前一个节点（反转）
            current.next = prev
            # 前一个节点移动到当前
            prev = current
            # 当前节点移动到下一个
            current = next_node

        # 最后 prev 就是新的头节点（此时 prev 节点就是反转前的最后一个节点）
        self.head = prev
        return True

    def clear(self) -> None:
        """
        清空链表：删除所有节点
        """
        self.head = None
        self.size = 0

    def to_list(self) -> list:
        """
        将链表转换为 Python 列表

        返回：
            链表转换为的列表
        """
        result = []
        current = self.head

        while current is not None:
            result.append(current.data)
            current = current.next

        return result
