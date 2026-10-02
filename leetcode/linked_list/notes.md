# 链表 · 章节笔记

> 对应题目：2 / 19 / 21 / 141 / 142 / 143 / 146 / 206 / 234（**进行中**）
>
> 另有基础练习：`linked_list_basics.py`（自写 Node / LinkedList + 头插 / 尾插 / 按位置插入 / 按值删除 / 按位置删除 / 按值查找 / 按位置获取 / **反转** / 清空 / 转列表）
>
> 更新时间：2026-10-02（演进式笔记，随刷题持续补充）

---

## 一、核心思想：链表的"物理画面"

| | 数组 | 链表 |
|---|---|---|
| 内存布局 | **连续**的一排格子 | **散落**在内存各处的节点 |
| 怎么找到第 k 个 | **算出来**：`地址 = 首地址 + k×格大小` → $O(1)$ | 只能从 `head` **顺着 `.next` 一步步走** → $O(k)$ |
| 每个元素知道什么 | 只有自己的值 | 自己的值 **+ 下一个节点的地址** |
| 谁指向它 | 谁都行（靠下标） | **只有它的前一个节点**（头结点靠 `head` 指针） |

> **一句话**：数组是"连续的排屋"，链表是"散落的房子，每家门口写着下一家的地址"。
>
> **链表只能单向走**：每个节点只知道"下一个"在哪，不知道"上一个"（这正是 206 要反转的原因）。

**演示过的证据**：三个节点的 `id()` 互不相邻。

## 二、⭐ 变量 vs 节点（理解链表的第一个关键）

> **变量是"标签 / 手指/书签"，不是"盒子"。**

```python
cur = head            # 标签 cur 贴到 head 指的节点上
cur = cur.next        # 标签 cur 挪到下一个节点 ——【移动的是名字，节点没变】
x = a                 # 又贴一个标签（不是复制！）
x.val = 777           # 同一个对象 → a.val 也变了
```

| 代码 | 动的是变量？ | 动的是节点？ |
|---|---|---|
| `cur = head` / `cur = cur.next` | ✅ 标签移动 | ❌ |
| `nxt = cur.next` | ✅ 标签移动 | ❌ |
| `cur.next = prev` | ❌ | ✅ **改了 cur 节点的箭头** |
| `new = Node(9)` | ✅ 新标签 | ✅ **造了个新节点** |
| `x = a` | ✅ 又贴一个标签 | ❌ |

**两个铁律**：
1. 节点上的一切都是属性：`.data` 存数据，`.next` 存箭头；
2. **改指针前必须先保存下一个** —— 否则 `cur.next = prev` 一覆盖，就再也找不到"下一家"了。

## 三、遍历三件套（背下来）

```python
cur = head                  # ① 起点：从 head 进去（链表没有下标）
while cur is not None:      # ② 条件：还没走到 None
    ...处理 cur.data...       # ③ 处理当前节点
    cur = cur.next          # ④ 前进 ——【唯一】的前进方式
```

**同一个模板换一行"处理"，就是不同的操作**：

| 目的 | 处理那一行 |
|---|---|
| 打印 | `result.append(str(cur.data))` |
| 求长度 | `count += 1` |
| 找尾节点 | 条件改成 `while cur and cur.next:` |
| 按值查找 | 条件改成 `while cur and cur.data != target:` |

⚠️ **最常见 bug：忘记写 `cur = cur.next` → 死循环。**

## 四、⭐ 一切操作都是"改 `.next`"——插入/删除的统一套路

**任何插入，都是同一套两步**：

```
① 让【新节点】的 next 指向"后面那部分"
② 让【前面那部分】指向新节点
```

| 插入位置 | ① 新节点指向 | ② 谁改指向新节点 |
|---|---|---|
| **头部**（头插） | `self.head`（原入口） | `self.head` |
| **中间**（`node` 之后） | `node.next` | `node.next` |
| **尾部**（尾插） | `None` | 原尾节点的 `.next` |

**顺序铁律：先「接」后「断」** —— 先把新节点挂上去，再改前面的指向。

**删除**：不需要"真的删掉"，**让前一个节点跳过它**即可：

```python
prev.next = prev.next.next      # 被跳过的节点没人指向 → Python 自动回收
```

**头插的指针细节**（唯一需要"改两处"的插入）：

```python
new_node.next = self.head   # ① 把入口的指向"抄一份"给新节点
self.head = new_node        # ② 把入口本身换成新节点
```

- **顺序绝对不能反**：反了会变成 `new_node.next = new_node`（**自环**）且原链丢失；
- **空链表天然兼容**：`new_node.next = None`，不用特判；
- **副作用：天然逆序**（依次头插 1,2,3 → 得到 3→2→1）—— 这是 206 的另一种解法思路。

## 五、头指针 `head` vs 虚拟头结点 `dummy`

| | **`head`（头指针）** | **`dummy`（虚拟头结点 / 哨兵）** |
|---|---|---|
| 本质 | 一个**变量/属性**（指针） | 一个**真实的 `Node` 对象** |
| 是节点吗 | ❌ 不是 | ✅ 是（有 `data`、`next`） |
| 存数据吗 | 不存 | 存，但是**占位值**，不参与业务 |
| 空链表时 | `head = None`（**可以悬空**） | 依然是个对象 |
| 作用 | 链表的**入口** | 给头结点**伪造一个前驱** |
| 用完 | 直接用它 | 要 `return dummy.next` |

**为什么判 `head` 不是节点**：空链表时 `head = None` —— **节点不可能是 `None`，指针可以是。**

**`dummy` 解决什么**：删/插头结点时不用特判，所有位置写法统一：

```python
dummy.next = dummy.next.next    # 删头结点
prev.next  = prev.next.next     # 删中间节点 —— 同一个写法！
```

> 后面 **21 / 19 / 2 / 143 / 146** 几乎都会用到 dummy。

### 5.1 ⚠️ 术语陷阱：「头结点」到底指谁？

> **头指针指向的节点 = 头节点**（宽泛说法，成立）。
> **但中文教材（严蔚敏《数据结构》）的「头结点」常专指「不存业务数据的虚拟节点」** —— 这时第一个数据节点叫「**首元节点**」。

| 术语 | 英文 | 本质 |
|---|---|---|
| **头指针** | head pointer | 一个**指针**（变量/属性），链表的入口，可以为 `None` |
| **头结点** | head node / dummy head | ⚠️ 中文教材多指**不存数据的占位节点**（= 力扣的 dummy / 哨兵） |
| **首元节点** | first node | 第一个**真正存业务数据**的节点 |

**两种约定对比**（`linked_list_basics.py` 用的是 A）：

```
【约定 A：不带头结点】= 力扣、我的实现
   head ──▶ [1] ──▶ [2] ──▶ [3] ──▶ None
            ↑ 首元节点，head.data = 1 就是业务数据

【约定 B：带头结点】= 教材常见写法
   head ──▶ [头结点] ──▶ [1] ──▶ [2] ──▶ [3] ──▶ None
            (data=None)  ↑ 首元节点
            head.data = None（读不到业务数据）
            head.next.data = 1（真数据从这里开始）
```

- 两者**逻辑内容完全一样**，区别只在「要不要在前面垫一个占位节点」；
- **判断法**：看 `head.data` 是不是业务数据 —— 是 → 约定 A；是 `None` / 占位值 → 约定 B。

**教材为什么用「带头结点」**：让「第一个位置」和「其他位置」的操作统一，不用特判 ——

| 操作 | 不带头结点（A） | 带头结点（B） |
|---|---|---|
| 插入/删除**第一个元素** | ❌ **要特判**（没有前驱） | ✅ 和中间一样，改 `head.next` |
| 空链表表示 | `head is None` | `head.next is None`（head 永不为 None） |

> 💡 **同一个东西，三种叫法**：教材的「带头结点的链表」= 力扣题解的 `dummy`（哨兵）= 给头结点**伪造一个前驱**。
>
> 力扣题目参数 `head` 一律是**约定 A**；需要时**临时造一个 dummy** 即可，不必整个链表都带头结点。

## 5.2 ⭐ 力扣的链表写法 vs 你自己写的链表类

| | **你写的**（`linked_list_basics.py`） | **力扣的** |
|---|---|---|
| 类 | `LinkedList`（容器）**+** `Node`（节点） | **只有 `ListNode`**（节点） |
| “头”在哪 | `self.head`，是**对象的属性** | 是**函数参数** `head` |
| 怎么开始遍历 | `self.head` | 直接用参数 `head` |
| 怎么交出结果 | 改 `self.head` | **必须 `return` 新头** |
| 字段名 | `data` / `next` | **`val`** / `next` |

**核心差异一句话**：

> **力扣：`head` 是参数，答案靠 `return`。**
> **你自己的类：`self.head` 是属性，改完不用 return。**

**为什么力扣不给容器类**：① 只考算法，容器 API 是噪音；② 判题机要好构造输入；③ 头的传递用参数最干净，不会残留状态。

**力扣的 `ListNode` 定义在注释块里**（`# Definition for singly-linked list.`），**不要自己重新定义** —— 这正是本地脚手架里的 `class ListNode` 必须注释掉的原因。

### ⚠️ 网页上的 `head = [1,2,3,4,5]` 不是列表！

那只是**展示格式**（JSON 里没法表达指针，用数组代替）。判题机的实际流程：

```
网页 [1,2,3,4,5]  --build()-->  ListNode 链  --你的函数-->  新头  --to_array()-->  网页 [5,4,3,2,1]
```

实测：`isinstance(head, list)` → `False`，**你收到的永远是 `ListNode`**。
二叉树题同理（`root = [3,9,20,null,null,15,7]` → 实际是 `TreeNode`）。

## 5.3 本地自测脚手架：`build` / `to_array`

链表骨架文件底部都带同一套脚手架（力扣环境自带 `ListNode`，**提交前记得注释掉**）：

```python
def build(arr):      # [1,2,3] -> 1->2->3（复刻判题机的构造过程）
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_array(head):  # 链表 -> [1,2,3]（方便和期望结果对照）
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
```

自测就变成一行：

```python
print(to_array(sol.reverseList(build([1, 2, 3, 4, 5]))))   # 期望 [5, 4, 3, 2, 1]
```

> 💡 `build` 里用的正是 `dummy` 哨兵 —— **提前预习了 21 / 19 / 2 的核心技巧**。
> 唯一例外：**有环的题（141 / 142）**没法用 `build` 造环，得手动接：`a = build([3,2,0]); a.next.next.next = a.next`。

## 六、基础操作实现要点（来自 `linked_list_basics.py`）

| 操作 | 关键点 | 复杂度 |
|---|---|---|
| `is_empty()` | `self.head is None` | $O(1)$ |
| `__len__()` | 返回**非负整数**；注意与 `size` 同步 | $O(1)$ |
| `__str__()` | **必须返回字符串**；遍历 + `append(str(x))` + `" -> ".join(...)` | $O(n)$ |
| `insert_at_head` | 改 2 个指针，**先接后断**；空链天然兼容 | $O(1)$ |
| `insert_at_tail` | 空链特判 → 遍历找尾 → 接上；**待优化：加 `self.tail` 可变 $O(1)$** | $O(n)$ |
| `insert_at_position` | **遍历到 `position - 1` 个节点**（不是 `position`！） | $O(n)$ |
| `delete_by_value` | 删头要特判；其余用 `current.next` 跳过一个 | $O(n)$ |

**`insert_at_position` 的 off-by-one 陷阱**：

```python
current, current_pos = self.head, 1
while current_pos < position - 1:   # ✅ 停在插入位置的【前一个】节点
    current = current.next
    current_pos += 1
# 之后：new_node.next = current.next; current.next = new_node
```

- 若写成 `while current_pos < position:` → 会多走一步：`position = size+1` 时 `current` 变成 `None` → **AttributeError**；`position` 在中间时会**插错位置**。

**⚠️ 维护 `self.size` 的纪律**：每次增删都要 `+1` / `-1`。漏了会**静默出错**（`len(obj)` 与实际不符，还会让 `bool(obj)` 与 `is_empty()` 矛盾）。

## 七、我踩过的坑（真实记录）

| # | 坑 | 现象 / 教训 |
|---|---|---|
| 1 | `self.stack.append` 类比——把 `self` 当容器 | `self` 不是 list，**继承 `object` 没有 `append`** |
| 2 | 链表节点写 `self.next = None` | Pylance 推断"只能是 None" → 后续赋值报错。**修法：`self.next: "Node \| None" = None`**（静态检查，不影响运行） |
| 3 | `insert_at_position` 缩进多了 4 格 | 变成**嵌套函数** → 类里调不到（`AttributeError`），**但不报语法错** |
| 4 | `__str__` 里 `return result`（返回列表） | `TypeError: __str__ returned non-string` |
| 5 | 拼接时漏了空格：`" ->".join(...)` | 输出 `'1 ->2 ->3'`；**用 `repr()` 才能看出** |
| 6 | 忘记更新 `self.size` | `len(lst)` 返回 0 但实际有 3 个节点（**静默错误**） |
| 7 | `insert_at_position` 的 off-by-one | 中间位置插错、`size+1` 直接崩溃 |
| 8 | 术语混淆：以为「头节点」就是「头结点」 | **头指针指向的节点**在宽泛意义上叫头节点；但教材的「头结点」多指**不存数据的虚拟节点**，此时第一个数据节点叫「**首元节点**」。**看 `head.data` 是不是业务数据**最可靠（详见 §5.1） |
| 9 | 在力扣 `Solution` 里写了 `self.head` | `AttributeError: 'Solution' object has no attribute 'head'`。**力扣没有容器类，`head` 是参数不是属性** → 用参数 `head` 开头，改头时用 `prev` / `dummy` 记录，最后 `return`（详见 §5.2） |
| 10 | 反转写成 `return head` | 循环后 `head` 已退化成**尾节点**，返回它只能得到一个节点。**必须 `return prev`**；但**空链表 / 单节点**要直接 `return head`（此时 `prev` 还是 `None`，返回它会把链丢丁） |
| 11 | `get_at_position` 里写 `while current < position` | 拿**节点对象**和 **int** 比大小 → `TypeError: '<' not supported between instances of 'Node' and 'int'`。应该比**计数变量**：`while current_pos < position`（而且取第 k 个要停在 k，不是 k-1，与插入/删除不同） |

## 八、易错点 / 自查清单

- [ ] 改指针前，**先保存 `nxt = cur.next`** 了吗？
- [ ] 插入的**顺序**是"先接后断"吗？
- [ ] 头结点 / 尾节点 / **空链表**这三种边界都处理了吗？
- [ ] `self.size` 或 `self.tail` 之类的**派生状态同步**了吗？
- [ ] 遍历条件用 `is not None`（而不是 `!= None`）吗？
- [ ] `__str__` **返回的是字符串**吗？
- [ ] 字符串拼接的**空格**对了吗？（`repr()` 检查）
- [ ] `def` 的**缩进**和别的 `def` 对齐吗？

## 九、复杂度速查（基础操作）

| 操作 | 数组 | 链表 |
|---|---|---|
| 访问第 k 个 | $O(1)$ | **$O(k)$** |
| 头部插入 | $O(n)$ | **$O(1)$** |
| 中间插入（已持有前驱） | $O(n)$ | **$O(1)$** |
| 中间删除（已持有前驱） | $O(n)$ | **$O(1)$** |
| 尾部插入（无 tail 指针） | $O(1)$（摊销） | **$O(n)$** |
| 遍历 / 找尾 | $O(n)$ | $O(n)$ |

> **链表用"随机访问慢"换来"插入删除快"** —— 这就是它存在的意义（146 LRU 正需要）。

## 十、待刷题目与各自的考察点

| # | 题目 | 难度 | 考察点 |
|---|---|---|---|
| 206 | Reverse Linked List | Easy | 三指针反转 / 递归；**一切链表题的地基** |
| 21 | Merge Two Sorted Lists | Easy | **dummy 哨兵**入门 |
| 141 | Linked List Cycle | Easy | 快慢指针判环 |
| 19 | Remove Nth Node From End | Medium | 快慢指针差 n 步 + 删头边界 |
| 142 | Linked List Cycle II | Medium | 环入口的**数学推导**（$a=c$） |
| 143 | Reorder List | Medium | 找中点 + 反转后半段 + 合并（一题三练） |
| 146 | LRU Cache | Medium | 哈希 + **双向链表**（对 LLM 应用岗尤其相关：缓存淘汰） |
| 2 | Add Two Numbers | Medium | 进位模拟 + dummy |
| 234 | Palindrome Linked List | Easy | 快慢找中点 + 反转后半段 |

> 进度：**206 代码已通过自测**（三指针原地反转，$O(n)$ 时间 / $O(1)$ 空间），待补 `# 解法 / 时间复杂度 / 空间复杂度` 三行注释后标记为 ✅。

## 十一、面试可以这么说

> "链表题的核心是**分清'移动标签'和'改箭头'**：`cur = cur.next` 只挪变量，`cur.next = prev` 才改结构。
> 第二个要点是**边界**：头结点没有前驱，所以我习惯加一个 `dummy` 哨兵把边界统一掉。
> 写指针操作时我会守住一条铁律——**改 `.next` 之前先把下一个存下来**，否则链会断。"

---

## 附：与 Python 类基础的关系

链表实现会连带用到一批 Python 类知识（`object` / `self` / `__init__` / 属性 / 变量 vs 对象 / 魔术方法 / 参数），
已单独沉淀在 **[`notes/python_oop_basics.md`](../../notes/python_oop_basics.md)**。
