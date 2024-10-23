# LeetCode 打卡记录

## 2024/10/17

###  704. 二分查找

[力扣题目链接(opens new window)](https://leetcode.cn/problems/binary-search/)

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

**Example 2:**

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```



**第一想法/python**

做了两遍这个题了，但乍一看还是会愣一下。思路应该是每次查看中间的元素，判断搜索区间是往左还是往右，随后再依次进行直到找到答案。想要while写<=, 那应该是左闭右开，right指针从len(nums)开始。

碎碎念：我只会python，我好菜啊，刷完一遍后要顺带学一下C好了orz。



写了，左闭右开while不是left<= right, 而是left< right!

写完后虽然快速debug了出来，但说明左闭右开的理解还是不扎实，靠熟练度写出来的。重新复习相关概念。



#### **左闭右开/左闭右闭** 

(感谢chatgpt)

**1. 左闭右开区间 `[left, right)`**

- **定义**：包含左端点 `left`，但不包含右端点 `right`，即 `[left, right)` 包含所有 `left <= x < right` 的值。
- **特点**：当 `left == right` 时，区间为空，因为区间的定义要求 `x` 小于 `right`，而当 `left == right` 时，没有任何值满足此条件。也就是说，这时已经没有可以再查找的元素了，所以在二分查找中，循环的终止条件是 `left < right`。

2. **左闭右闭区间 `[left, right]`**

- **定义**：包含左端点和右端点，即 `[left, right]` 包含所有 `left <= x <= right` 的值。
- **特点**：当 `left == right` 时，区间依然包含一个元素，就是 `left` 和 `right` 相同的这个点，因此在二分查找中可以继续进行一次比较。循环的终止条件通常是 `left > right`。

**为什么在左闭右开中 `left == right` 是没有意义的？**

在左闭右开的区间中，区间的定义是包含左端点而不包含右端点，也就是说区间里的元素是 `[left, right)`，当 `left == right` 时，区间的范围变成 `[left, left)`，这表示区间内没有任何元素。所以如果 `left == right` 时再继续查找是没有意义的，因为已经没有可以检查的元素了。



用左闭右闭写了一下C++语言的这道题，不涉及什么复杂的操作，挺简单的。 学会了一下&的语法。



#### C++： &的用法

**引用传递 vs 值传递**：

- **值传递**：如果不使用 `&`，即写成 `vector<int> nums`，那么当调用这个函数时，整个 `nums` 数组会被复制一份传递给函数。在函数内部对 `nums` 的任何修改都不会影响原数组，因为操作的只是该数组的副本。这种方式在处理大型数组或复杂对象时会非常消耗内存和时间。
- **引用传递**：使用 `&` 传递引用后，函数将直接操作传入的原数组，而不是它的副本。这样不仅节省了内存，还使得函数内部的操作能够直接影响原数组。例如，如果你在函数内部修改了 `nums`，这些修改也会反映到函数外的原数组。

**`vector<int>& nums` 的含义**：

- `vector<int>` 是一个整数类型的动态数组（向量），它可以存储多个 `int` 类型的值。
- `&` 表示 `nums` 是一个引用，这意味着函数不会复制 `nums`，而是直接操作原始的数组（向量）。
- `nums` 是传入的数组的名称。



------

### 27 移除元素



第一想法：
用快慢指针，遇到一个val就fast+1，然后把fast的元素替换进slow的元素里面去。

debug：

想法基本正确，出现了快慢指针同步+1时没有判断item!=val的错误，导致碰见了相同的元素也会同步+1，导致out of range.



-----



### 209 长度最小的子数组

第一想法：

滑动窗口

窗内数值总和 < target，right+1。

sum > target, left+1

sum = target, sum_registor = min(sum_registor, sum). 然后left+1, right+1



Debug：

当代码遇到边界条件时，就会掉链子。



```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        reg = float('inf')
        sum = 0 + nums[0]

        while right <= len(nums) - 1:
            if sum < target:
                right += 1
                sum += nums[right]
            elif sum > target:
                sum -= nums[left]
                left += 1
            else:
                reg = min(reg,sum)
                right += 1
                sum += nums[right]
                sum -= nums[left]
                left += 1
        return reg
print(Solution().minSubArrayLen(7,[2,3,1,2,4,3]))
```



```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = 0
        min_l = float('inf')
        cur_sum = 0

        while right <= len(nums) - 1:
            cur_sum += nums[right]

            while cur_sum >= target:
                min_l = min(min_l,right - left +1)
                cur_sum -= nums[left]
                left += 1
            
            right += 1
        
        return 0 if min_l == float('inf') else min_l

```





# 2024.10.20 打卡

###  **203.移除链表元素**  

第一反应:

设置dummy head, 然后检测current的next，如果current的next为目标val，则把next指向next.next. 如果没有next.next，则指向None

犯的错：

while 检测的是current而不是current.next，导致current指向最后一个节点的时候，current.next.val会出现报错。因为None是没有val的。这一题主要所关注的是current.next的属性，如果没有下一节点的话就不用继续执行操作了。



### 707 设计链表

设计得很想死

写起来很毛躁，写得不清晰，打算之后重做



### 206 反转链表

犯的错1:

直接设置prev为head, current = head.next

这会导致第二个节点往前指的时候，第一个节点的next仍然指向2nd节点，导致死循环cycle.

所以要先设定prev为none, 把1st node 的节点往前指向None，再往下做操作。



犯的错2：

return 个皮球的head, return prev去。



###  **24. 两两交换链表中的节点** 

一开始忘记使用虚拟节点了，愣头青了一下。当需要返回一大串链表的时候，虚拟节点还是很关键的。要记得使用。

这里debug的点主要在于移动current节点的时候，要注意移动的下一个节点对于下一套交换流程的相对位置。然后while要检测next.next.next，其余就没什么问题了。



### 19 **删除链表的倒数第N个节点**  

双指针的fast 和 slow，我一开始错误理解为slow 和fast的指针含义分别对应为prev和next，这样在移动后也可以保持固定的相对关系。但其实这是错误的，因为相对关系其实不管怎样都一样，都是跳过一个节点进行链接。关键还是在于移动的次数。

其核心思想不在于slow和fast对node的映射关系，而是在于其相对关系可以保证在移动后，slow的位置可以固定在待删除节点的前一位，也就是通过移动让slow代替掉fast，而fast则指向none。



###  **面试题 02.07. 链表相交**  

这一题主要的思想在于对齐链表，然后同时移动检查有没有相同节点。

debug时，主要错在没看清楚题目，总是在return val或者是int。还是要看清楚需求啊。



###  **142.环形链表II**  

还是需要用数学思维来写题。

自己写的时候预料到了要让slow和fast同时行进，来等待相遇。但是画图的时候错以为相遇的地方.next就是循环的入口，其实那只能证明fast经过了一个循环追上了slow而已。只能够证明“这里有循环存在”，只完成了第一步。



第二步才是去寻找环形链表里的入口在什么地方的时候，需要通过画图和计算得到。

理解完后还是不难的。Debug稍微花了点时间，while条件总是写得不好SOS。

