# Python 面向对象基础 · 专题笔记

> 来源：刷 155 最小栈 / 链表时提出的一系列问题（`object` 是什么、`self` 是什么、`__init__` 干嘛的、参数为什么数量不匹配……）
>
> 位置说明：这份是**跨题型**专题，放在根目录 `notes/`；各题型自己的笔记在 `leetcode/<题型>/notes.md`。
>
> 更新时间：2026-10-02

---

## 一、类与对象：图纸 与 实例

```python
class ListNode(object):        # 图纸（定义一个新类型）
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

n = ListNode(5)                # 按图纸造出一个实例
```

| 概念 | 说明 |
|---|---|
| **类（class）** | 图纸 / 模板 —— 描述"这种对象长什么样" |
| **对象 / 实例（object / instance）** | 按图纸造出来的实体，各占一块内存 |
| **属性（attribute）** | 对象身上的"格子"：`n.val`、`n.next` |
| **方法（method）** | 定义在类里的函数，第一个参数固定是 `self` |

## 二、`object` 是"所有类的老祖宗"

```python
class A(object):   # 老风格
class A:           # Python 3 里完全等价
```

- `object` 是 Python 里最顶端的类，**所有类最终都继承它**；
- 括号里写的是**要继承的父类** —— **继承谁，就白拿谁的能力**：

| 写法 | 白拿到什么 |
|---|---|
| `class A(object)` / `class A` | 只有"普通对象"最基本的能力 |
| `class A(list)` | **全部 list 方法**：`append` / `pop` / 切片… |
| `class A(dict)` | 全部 dict 方法 |

验证方式：

```python
issubclass(A, object)   # True（不写括号也是）
A.__mro__               # (<class 'A'>, <class 'object'>)  ← 继承链
```

> **`(object)` 是 Python 2 遗留写法**：那时 `class A:` 是"旧式类"、`class A(object):` 才是"新式类"。**Python 3 已统一，写不写一样。**

### ⭐ 由此解释一个 155 的坑

```python
class MinStack(object):
    ...
    self.append(val)          # ❌ AttributeError: 'MinStack' object has no attribute 'append'
    self.stack.append(val)    # ✅ 因为 self.stack 才是真正的 list
```

**`self` 不是 list**（`MinStack` 只继承 `object`），所以它身上没有 `append`。想用 list 的能力，就得先在对象里**放一个 list**。

## 三、`self` 是什么

> **`self` = "当前这个对象本身"**，由 Python 自动传入，你调用时不用写。

```python
s = MinStack()
s.push(3)          # Python 实际执行 MinStack.push(s, 3)
```

对照 Java/C++：`self` 相当于 `this`，但**必须显式写在参数列表第一个**。

## 四、`__init__`（初始化）与 `__new__`（创建）

**`Node(7)` 的背后是两阶段：**

```
Node(7)
 ├─ ① __new__(cls)      → 造出一个【空对象】{}
 └─ ② __init__(self, 7) → 给它挂上属性
```

| | `__new__(cls, ...)` | `__init__(self, ...)` |
|---|---|---|
| 职责 | **创建**对象 | **初始化**对象 |
| 第一个参数 | **`cls` = 类**（此刻实例还不存在） | **`self` = 刚造好的实例** |
| 返回值 | 必须返回那个对象 | 必须返回 `None` |
| 你要写吗 | ❌ 几乎永远不写 | ✅ 经常写 |

- `__init__` 的职责：**用 `self.xxx = ...` 给对象挂初始属性**（"出厂设置"）；
- 名字必须一字不差（`__init__`），写成 `init` 就不会被自动调用；
- 不写 `__init__` 也能跑，只是对象创建后**没有初始属性**；
- `__init__` 里还能做校验、预计算等；
- 只有继承**不可变类型**（`int` / `str` / `tuple`）时，才需要自己写 `__new__`。

**手动掀盖子（只为了理解，日常不用）：**

```python
n2 = Node.__new__(Node)      # ① 造空对象
Node.__init__(n2, 7)         # ② 初始化（n2 就是 self）
```

## 五、属性：`self.xxx` 才是"存进对象"

```python
def __init__(self):
    self.kept = []      # ✅ 挂在对象上 → 对象活着它就在，所有方法都能访问
    thrown = []         # ❌ 只是局部变量 → 方法结束就销毁
```

验证：`obj.__dict__` 里**只有 `kept`，没有 `thrown`**。

**对象内部就是一个字典**：

```
s.__dict__ == {'stack': [...], 'min_stack': [...]}
self.stack  ≡  self.__dict__['stack']
```

### 三个必须分清的点

| 事实 | 说明 |
|---|---|
| **属性名是你自己起的** | `self.stack` / `self.data` 都行，只要前后一致 |
| **属性是"标签"不是"盒子"** | `self.a = []` 和 `self.b = {}` 是**两个独立对象** |
| **`= []` 是"贴标签"，不是"复制"** | `self.b = self.a` → 两个标签指向**同一个**对象（别名，改一个动两个） |

检测是否同一个对象：`a is b` / `id(a) == id(b)`。

### ⭐ 引用独立 ≠ 逻辑同步

155 里 `self.stack` 和 `self.min_stack` 是**两个独立列表**（`is` 为 False），但"**长度必须一致**"是**你的代码**要负责维护的约定 —— Python 不会帮你检查。

这就是下面这个 bug 的根源：

```python
M.stack.pop()      # ❌ 只弹主栈，辅助栈没动 → 两栈长度不一致 → getMin 返回错误值（还不报错！）
M.pop()            # ✅ 走公开接口，两个栈同步弹
```

### 接口 vs 内部

| 位置 | 写法 | 说明 |
|---|---|---|
| 类**内部**（`__init__`、方法里） | `self.stack` ✅ | 操作自己的数据 |
| 类**外部**（`M = MinStack()` 之后） | `M.stack` ⚠️ | 越界访问内部实现，应改用 `M.pop()` |

想在命名上提示"内部"，可以写 `self._stack`（**约定**，不强制）。

## 六、⭐ 变量 vs 对象：链表理解的关键

> **变量是"标签 / 手指"，不是"盒子"。** 赋值是"贴标签"，不是"复制内容"。

```python
cur = head            # 标签 cur 贴到 head 指的节点上
cur = cur.next        # 标签 cur 挪到下一个节点 ——【移动的是名字，节点本身没变】
x = a                 # 又贴一个标签（不是复制！）
x.val = 777           # 因为 x 和 a 是同一个对象 → a.val 也变成 777
```

| 代码 | 动的是变量？ | 动的是节点？ |
|---|---|---|
| `cur = head` / `cur = cur.next` | ✅ 标签移动 | ❌ |
| `nxt = cur.next` | ✅ 标签移动（存了个地址） | ❌ |
| `cur.next = prev` | ❌ | ✅ **改了 cur 节点的箭头** |
| `cur.val = 5` | ❌ | ✅ 改了 cur 节点的数据 |
| `new = ListNode(9)` | ✅ 新标签 | ✅ **造了个新节点** |
| `x = a` | ✅ 又贴一个标签 | ❌ |

**链表的两个铁律**（由此推出）：

1. **节点上的一切都是属性**：`.val` 存数据，`.next` 存箭头；
2. **改指针前必须先保存下一个** —— 因为 `cur.next = prev` 会覆盖掉原来的箭头，之后就找不到"下一家"了：
   ```python
   nxt = cur.next     # ① 先存
   cur.next = prev    # ② 再改
   ```

## 七、函数 / 方法的参数

### 默认值让参数可选

```python
def __init__(self, val=0, next=None):
```

| 参数 | 有默认值？ | 你要传吗 |
|---|---|---|
| `self` | ——（自动） | ❌ 永远不用 |
| `val=0` | ✅ | 可选 |
| `next=None` | ✅ | 可选 |

所以这几种调用都合法：

| 调用 | `val` | `next` |
|---|---|---|
| `ListNode()` | 0（默认） | `None`（默认） |
| `ListNode(99)` | 99 | `None`（默认） |
| `ListNode(99, b)` | 99 | b |
| `ListNode(next=b)` | 0（默认） | b ← **关键字传参，跳过了 val** |

### 参数绑定顺序（4 步）

```
① 位置参数从左往右填  →  ② 关键字参数按名字填  →  ③ 剩下的用默认值  →  ④ 还缺就 TypeError
```

| 想省略的位置 | 位置传参 | 关键字传参 |
|---|---|---|
| **最右边**的（有默认值） | ✅ | ✅ |
| **中间**的（有默认值） | ❌ **做不到** | ✅ |
| **最左边**的（无默认值） | ❌ 报错 | ❌ 报错 |

**规则**：
- 位置传参只能"**从尾部砍掉**"，你传的值绝不会跳到后面去；
- 有默认值的参数**必须写在后面**（`def f(a=0, b)` 是 `SyntaxError`）；
- 位置参数必须写在关键字参数前面。

## 八、魔术方法（dunder，前后各两个下划线）

**机制：你调 `len(x)`，Python 自动去调 `x.__len__()`** —— 是**按名字找钩子**，不是装饰。

**反证**：方法名叫 `len`（少了下划线）时，`c.len()` 能跑，但 `len(c)` 报
`TypeError: object of type 'C' has no len()`。

**为什么用双下划线**：`__xxx__` 是**解释器保留的名字空间** —— 避免"你的普通方法"和"内置函数要调的钩子"撞名。你的方法叫 `size`、`length` 都随便，绝不干扰 `len()`。

### 四种下划线形式

| 形式 | 例子 | 含义 |
|---|---|---|
| `name` | `size` | 普通 |
| `_name` | `_size` | **约定**：内部使用（不强制） |
| `__name` | `__size` | **名称改写**（name mangling），防子类冲突 |
| **`__name__`** | **`__len__`** | **Python 保留的魔术方法** |

### 常用魔术方法 ↔ 语法

| 魔术方法 | 自动支持的语法 |
|---|---|
| `__init__` | `Obj(...)` 创建对象 |
| `__len__` | `len(obj)` ← **必须返回非负整数** |
| `__getitem__` | `obj[i]` |
| `__setitem__` | `obj[i] = x` |
| `__iter__` | `for x in obj` |
| `__contains__` | `x in obj` |
| `__str__` | `print(obj)` / `str(obj)` ← **必须返回字符串** |
| `__eq__` | `obj1 == obj2` |
| `__add__` | `obj1 + obj2` |

**术语**：这叫**协议（protocol）** —— 在 Python 里"支持某种操作"取决于**有没有实现对应魔术方法**，而**不是**继承自哪个类（与 Java 接口完全不同）。

**两条纪律**：
1. `__len__` 必须返回**非负整数**，`__str__` 必须返回**字符串**，否则 TypeError；
2. **不要自己发明 `__xxx__` 形式的名字** —— 那是留给解释器的。

## 九、什么时候该写类

| 场景 | 建议 |
|---|---|
| 题目要求"对象 + 一组方法"（155 MinStack、146 LRUCache） | ✅ 写类 |
| 需要**在多次调用之间保持状态** | ✅ 写类 |
| 纯计算、无状态（20 有效的括号） | ❌ 一个函数就够，别为用类而用类 |

**判断法**：问自己"**这个对象需不需要记住状态？**"
- 155 的 `MinStack` 需要 → 有 `__init__` 准备两个空列表；
- 链表题的 `Solution` **不需要** → 没有 `__init__`（节点是从参数 `head` 传进来的）。

## 十、常见错误清单（都是真实踩过的）

| # | 错误 | 症状 / 原因 |
|---|---|---|
| 1 | `self.append(x)` | `AttributeError` —— `self` 不是 list；继承 `object` 没有 `append` |
| 2 | 忘记在 `__init__` 里初始化属性 | `AttributeError: 'X' object has no attribute 'yyy'` |
| 3 | 漏写 `self.` | 只是局部变量，方法结束就没了 |
| 4 | `self.b = self.a` 以为是复制 | 其实是**别名**，改一个动两个 |
| 5 | 可变类属性 `items = []`（写在 class 里） | 所有实例**共享**这个列表 → 互相污染 |
| 6 | 忘传无默认值的参数 | `missing 1 required positional argument` |
| 7 | 有默认值的参数写在前面 | `SyntaxError: non-default argument follows default argument` |
| 8 | `M.stack.pop()` 绕过接口 | 引用独立但逻辑被破坏 → **静默出错**（不报错但答案错） |
| 9 | `list.sorted()` | 不存在；`sorted()` 是内置函数、`.sort()` 是列表方法 |
| 10 | `__str__` 返回非字符串 | `TypeError: __str__ returned non-string` |
| 11 | `" -> ".join([1,2,3])` | `join` 只吃字符串，Python 不自动转换 |
| 12 | 自己写 `def __foo__` | 可能与将来 Python 官方的名字冲突 |
| 13 | `while` 条件里的变量在循环体里不更新 | **死循环 / IndexError**（567、20 都踩过） |
| 14 | 字符串拼接时多打/漏打空格 | 如 `'1 ->2 ->3'`；用 `repr()` 才能看出 |
| 15 | 用 `is` 比较数字/字符串的**值** | 结果依赖 CPython 缓存，不可靠 |
| 16 | 方法缩进多了 4 格 | 变成**嵌套函数**，类里调不到（`AttributeError`），但**不报语法错** |
| 17 | 维护了 `size` 却忘记同步 | `len(obj)` 与实际不符，**静默出错** |

## 十一、一句话总结

> **类 = 图纸；对象 = 按图纸造出的实例；`self` = 当前实例；`__init__` = 出厂设置（挂属性）。**
> **变量是标签不是盒子 —— 所以要分清"移动标签"和"改对象属性"，这是理解链表指针操作的前提。**
> **魔术方法（`__len__` / `__str__` / `__iter__`…）是 Python 认的"钩子名字"，实现了就自动支持对应语法。**

---

## 十二、`is` 与 `==`：身份 vs 值

| | `==` | `is` |
|---|---|---|
| 比什么 | **值**是否相等（调用 `__eq__`） | 是不是**同一个对象**（身份/id） |
| 例 | `[1,2] == [1,2]` → **True** | `[1,2] is [1,2]` → **False** |

**选择规则**：

- 比**值** → `==`
- 比**是不是同一个对象** → `is`
- **判 `None` → 一定用 `is None` / `is not None`**（PEP 8 推荐：更快，且不受自定义 `__eq__` 干扰）
- **绝不要用 `is` 比较数字/字符串的值**

**为什么不能用 `is` 比值** —— 结果依赖 CPython 实现细节：

```python
256 is int("256")                   # True   （小整数缓存 -5~256）
257 is int("257")                   # False  （超出缓存，新对象）
x, y = 257, 257                     # x is y → True！（同一行的字面量被编译器复用）
"hello" is "hel" + "lo"             # True   （编译期就拼好）
"hello" is "".join(["hel", "lo"])   # False  （运行期才拼）
# 但它们的 == 永远都是 True
```

> 链表的遍历条件 `while cur is not None` 就是 `is` 的正当用法。

## 十三、真假判定（truthiness）

**Python 里任何对象都能做真假判断**（`if x:` / `while x:` / `bool(x)`）。

**为假（falsy）就三类**：

| 类别 | 例子 |
|---|---|
| `None` | `None` |
| 各种**零** | `0`、`0.0`、`0j`、`False` |
| 各种**空容器** | `""`、`[]`、`()`、`{}`、`set()`、`range(0)` |

**反直觉但为真的**：

| 值 | 真假 | 原因 |
|---|---|---|
| `-1` | **True** | 非零（负数也是真） |
| `"0"` / `"False"` / `"None"` | **True** | 非空字符串 |
| `" "`（一个空格） | **True** | 非空字符串 |
| `[0]` / `(0,)` | **True** | 非空容器 |
| `float("nan")` | **True** | 非零 |

> **口诀：“空”和“零”才是假；字符串 `"0"` 因为长度不为 0，为真。**

**自定义对象**：默认 True，除非：
- 定义了 `__bool__` 且返回 False，或
- **定义了 `__len__` 且返回 0** ← 实现了 `__len__` 的类（如 LinkedList）自动获得真假判断

⚠️ **隐患**：`__len__` 影响真假 → 若内部的 `size` 忘记同步，`if obj:` 与 `obj.is_empty()` 会**互相矛盾**。

## 十四、类型注解与 Pylance 推断

```python
self.next = None        # Pylance 推断：self.next 的类型就是 None
new_node.next = head    # ❌ 报错：Node | None 不能赋给“只能是 None”的属性
```

**这不是运行时错误**（Python 运行时根本不检查类型），只是编辑器警告。修法：

```python
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next: "Node | None" = None      # ✅ 显式注解

class LinkedList(object):
    def __init__(self):
        self.head: "Node | None" = None      # ✅ 有了它，current.next 也不再报错
```

> 力扣模板里的 `Optional[ListNode]` **就是 `ListNode | None`**。

## 十五、缩进层级：方法必须写在类里

```python
class LinkedList:
    def insert_at_tail(self):
        ...
        def insert_at_position(self):   # ❌ 8 个空格 → 嵌套在方法内部的函数
            ...
```

后果：**不报语法错、程序照跑**，但 `lst.insert_at_position(...)` →
`AttributeError: 'LinkedList' object has no attribute 'insert_at_position'`。

> Java 靠大括号定层级，**Python 靠缩进**。每写完一个方法，扫一眼它的 `def` 是否与其它 `def` 对齐。

## 十六、字符串：不可变 / join / 空格

**① 不可变 ≠ 不能运算**

```python
a = "hello"
b = a
a = a + " world"    # 造出一个【新】字符串，a 改指向它
print(b)            # "hello"  ← b 没变，证明原对象没被修改
```

**② 空格是字符、占一位**

```python
len("a b")     # 3
list("a b")    # ['a', ' ', 'b']
repr("a b")    # 'a b'   ← 用 repr() 让不可见字符现形（排查字符串 bug 第一招）
```

**③ `join` 用法**：`胶水.join(一串字符串)` —— 胶水在前，只加在中间，元素**必须都是字符串**

```python
" -> ".join(["1", "2", "3"])   # '1 -> 2 -> 3'
"".join(["a", "b"])             # 'ab'
```

**④ `__str__` 里的典型数据流**

```
链表 → 遍历 append(str(node.data)) → ["1","2","3"] → " -> ".join(...) → "1 -> 2 -> 3"
```

> 所以 `str()` 是给 **`join`** 用的，不是给 `append` 用的（`append` 对类型毫无要求）。
