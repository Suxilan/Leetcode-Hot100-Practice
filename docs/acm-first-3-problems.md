# ACM 笔试训练第一组：链表 + 双指针 + 滑动窗口

## 1. 题型分类总览

| 序号 | 题型 | LeetCode 题号 | 题目 | 难度 | 高频考点 |
|---|---|---:|---|---|---|
| 1 | 链表反转 | 206 | Reverse Linked List | Easy | 指针操作、原地反转 |
| 2 | 双指针 | 283 | Move Zeroes | Easy | 快慢指针、稳定重排 |
| 3 | 滑动窗口 | 3 | Longest Substring Without Repeating Characters | Medium | 哈希计数、窗口收缩 |

---

## 2. 题目设计（ACM 输入输出版）

### 题目 1：链表反转（LeetCode 206）

**题意（ACM 版）**
- 输入一个整数数组，表示单链表节点值，输出反转后的链表。

**输入格式**
- 第一行：整数 `n`，表示节点个数。
- 第二行：`n` 个整数，表示链表节点值。

**输出格式**
- 一行输出反转后的链表节点值，空格分隔。

**样例 1**
- 输入：
```
5
1 2 3 4 5
```
- 输出：
```
5 4 3 2 1
```

**样例 2（边界）**
- 输入：
```
0

```
- 输出：
```

```

**Python（ACM 模式）参考实现**
```python
import sys


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    arr.reverse()
    if arr:
        print(*arr)


if __name__ == "__main__":
    solve()
```

**复杂度**
- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`（不计输入存储）

---

### 题目 2：移动零（LeetCode 283，双指针）

**题意（ACM 版）**
- 给定一个数组，将所有 `0` 移动到数组末尾，保持非零元素相对顺序。

**输入格式**
- 第一行：整数 `n`。
- 第二行：`n` 个整数。

**输出格式**
- 一行输出调整后的数组。

**样例 1**
- 输入：
```
5
0 1 0 3 12
```
- 输出：
```
1 3 12 0 0
```

**样例 2**
- 输入：
```
4
0 0 0 1
```
- 输出：
```
1 0 0 0
```

**Python（ACM 模式）参考实现**
```python
import sys


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    nums = list(map(int, data[1:1 + n]))

    slow = 0
    for fast in range(n):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    if n > 0:
        print(*nums)


if __name__ == "__main__":
    solve()
```

**复杂度**
- 时间复杂度：`O(n)`
- 空间复杂度：`O(1)`

---

### 题目 3：无重复字符的最长子串（LeetCode 3，滑动窗口）

**题意（ACM 版）**
- 给定一个字符串 `s`，输出不含重复字符的最长子串长度。

**输入格式**
- 一行字符串 `s`（可为空串）。

**输出格式**
- 一行输出最长长度（整数）。

**样例 1**
- 输入：
```
abcabcbb
```
- 输出：
```
3
```

**样例 2**
- 输入：
```
bbbbb
```
- 输出：
```
1
```

**样例 3**
- 输入：
```
pwwkew
```
- 输出：
```
3
```

**Python（ACM 模式）参考实现**
```python
import sys


def solve() -> None:
    s = sys.stdin.readline().rstrip("\n")

    left = 0
    last_pos = {}
    ans = 0

    for right, ch in enumerate(s):
        if ch in last_pos and last_pos[ch] >= left:
            left = last_pos[ch] + 1
        last_pos[ch] = right
        ans = max(ans, right - left + 1)

    print(ans)


if __name__ == "__main__":
    solve()
```

**复杂度**
- 时间复杂度：`O(n)`
- 空间复杂度：`O(k)`，`k` 为字符集大小

---

## 3. 解法归纳（笔试速记）

### 链表反转（206）
- 核心：三指针 `prev / cur / nxt`。
- 步骤：保存后继 -> 反转指向 -> 双指针前移。
- 易错点：先保存 `nxt`，否则链断。

### 双指针（283）
- 核心：`slow` 指向下一个应放非零元素的位置。
- `fast` 遍历数组，遇到非零就和 `slow` 交换并 `slow += 1`。
- 易错点：必须保持相对顺序，不能简单排序。

### 滑动窗口（3）
- 核心：窗口内字符不重复。
- 用哈希表记录字符最近位置；若重复且在窗口内，移动 `left`。
- 易错点：`left = max(left, last_pos[ch] + 1)` 的思想要保留（本实现用条件判断等价实现）。

---

## 4. 本组训练建议

1. 限时 30 分钟手写三题 ACM 输入输出。
2. 第二轮只写核心逻辑，不看模板。
3. 第三轮把三题抽象成可复用模板：
   - 链表指针模板
   - 双指针稳定重排模板
   - 滑窗去重模板
