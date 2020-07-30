<!-- TOC -->
- [1. all](#1-all)
    - [1.1. 1](#11-1)
    - [1.2. 2](#12-2)
    - [1.3. 3](#13-3)
<!-- /TOC -->
# all
<a id="markdown-all" name="all"></a>
## 1
<a id="markdown-1" name="1"></a>
```py
class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        _list = sorted(A,key=lambda i:i)
        self._sum = 0
        def dfs(_list,start,_res):
            if len(_res) >= 2:
                self._sum = self._sum + _res[-1] - _res[0]
            for i in range(start,len(_list)):
                _res.append(_list[i])
                dfs(_list,i+1,_res)
                _res.pop()
        dfs(_list,0,[])
        return self._sum % (10**9 + 7)
"""
  子序列(忽略单元素):  宽度:        
    [i0 i1]           i1-i0
    [i0 i2]           i2-i0
    [i0 i3]           i3-i0
    [i0 i4]           i4-i0
    [i1 i2]           i2-i1
    [i1 i3]           i3-i1
    [i1 i4]           i4-i1
    [i2 i3]           i3-i2
    [i2 i4]           i4-i2
    [i3 i4]           i4-i3
    [i0 i1 i2]        i2-i0
    [i0 i1 i3]        i3-i0
    [i0 i1 i4]        i4-i0
    [i0 i2 i3]        i3-i0
    [i0 i2 i4]        i4-i0
    [i0 i3 i4]        i4-i0
    [i1 i2 i3]        i3-i1
    [i1 i2 i4]        i4-i1
    [i1 i3 i4]        i4-i1
    [i2 i3 i4]        i4-i2
    [i0 i1 i2 i3]     i3-i0
    [i0 i1 i2 i4]     i4-i0
    [i0 i1 i3 i4]     i4-i0
    [i0 i2 i3 i4]     i4-i0
    [i1 i2 i3 i4]     i4-i1
    [i0 i1 i2 i3 i4]  i4-i0
    统计结果:
    宽度:     次数
    i4-i0    8
    i4-i1    4
    i3-i0    4
    i4-i2    2
    i3-i1    2
    i2-i0    2
    i4-i3    1
    i3-i2    1
    i2-i1    1
    i1-i0    1
    可以看到每种宽度出现次数 = 2**(右下标 - 左下标 - 1)
    进一步发现,按次数统计:
    右下标 - 左下标 - 1 = :               合并后:
    0 [i1-i0, i2-i1, i3-i2, i4-i3]  ->  i4-i0
    1 [i2-i0, i3-i1, i4-i2]         ->  i4-i0 + i3-i1
    2 [i3-i0, i4-i1]                ->  i4-i0 + i3-i1
    3 [i4-i0]                       ->  i4-i0
    res = ((i4-i0) << 0) + ((i4-i0 + i3-i1) << 1) + ((i4-i0 + i3-i1) << 2) + ((i4-i0) << 3)
    设n为A的最大下标
    mid = n / 2 分界点
    factor为i4-i0, i4-i0 + i3-i1 ... 等因子
    遍历range(n),当i小于mid时,factor累加,大于mid时递减,等于mid不动
作者：desti
链接：https://leetcode-cn.com/problems/sum-of-subsequence-widths/solution/zhu-bu-shou-si-ban-by-desti/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
https://leetcode-cn.com/problems/sum-of-subsequence-widths/solution/zi-xu-lie-kuan-du-zhi-he-by-leetcode/
"""
```
## 2
<a id="markdown-2" name="2"></a>
给你一个数组 nums，请你从中抽取一个子序列，满足该子序列的元素之和 严格 大于未包含在该子序列中的各元素之和。
如果存在多个解决方案，只需返回 长度最小 的子序列。如果仍然有多个解决方案，则返回 元素之和最大 的子序列。
与子数组不同的地方在于，「数组的子序列」不强调元素在原数组中的连续性，也就是说，它可以通过从数组中分离一些（也可能不分离）元素得到。
注意，题目数据保证满足所有约束条件的解决方案是 唯一 的。同时，返回的答案应当按 非递增顺序 排列。
 
示例 1：
输入：nums = [4,3,10,9,8]
输出：[10,9]
解释：子序列 [10,9] 和 [10,8] 是最小的、满足元素之和大于其他各元素之和的子序列。但是 [10,9] 的元素之和最大。 
示例 2：
输入：nums = [4,4,7,6,7]
输出：[7,7,6]
解释：子序列 [7,7] 的和为 14 ，不严格大于剩下的其他元素之和（14 = 4 + 4 + 6）。因此，[7,6,7] 是满足题意的最小子序列。注意，元素按非递增顺序返回。  
示例 3：
输入：nums = [6]
输出：[6]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```py
class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        _list = sorted(nums,key=lambda i:i)
        self.targe = target
        self._sum = 0
        def dfs(_list,start,_res):
            for i in range(start,len(_list)):
                if _list[i] > self.targe: break
                _res.append(_list[i])
                if _res[0] + _res[-1] <= self.targe:
                    self._sum = self._sum + 1
                    dfs(_list,i+1,_res)
                _res.pop()
        dfs(_list,0,[])
        return self._sum % (10**9 + 7)
```
## 3
<a id="markdown-3" name="3"></a>
我们有两个长度相等且不为空的整型数组 A 和 B 。
我们可以交换 A[i] 和 B[i] 的元素。注意这两个元素在各自的序列中应该处于相同的位置。
在交换过一些元素之后，数组 A 和 B 都应该是严格递增的（数组严格递增的条件仅为A[0] < A[1] < A[2] < ... < A[A.length - 1]）。
给定数组 A 和 B ，请返回使得两个数组均保持严格递增状态的最小交换次数。假设给定的输入总是有效的。
示例:
输入: A = [1,3,5,4], B = [1,2,3,7]
输出: 1
解释:
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。
注意:
A, B 两个数组的长度总是相等的，且长度的范围为 [1, 1000]。
A[i], B[i] 均为 [0, 2000]区间内的整数。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-swaps-to-make-sequences-increasing
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```py
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        i,j = 0,0
        
```