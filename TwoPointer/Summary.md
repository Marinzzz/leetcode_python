## 这个专题总结一下遇到过的

### Hard


### medium 


### easy

#### 合并两个有序数组
这道题要达到最优的时间复杂度和空间复杂度，需要使用指针法
```python
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        if not nums1:
            return nums2
        len_1 = len(nums1)
        len_2 = len(nums2)
        pointer_1 = len_1 - 1
        pointer_2 = len_2 - 1
        for i in range(len_1 + len_2 - 1, -1, 0):
            if nums1[pointer_1] > nums2[pointer_2]:
                nums1[i] = nums1[pointer_1]
                pointer_1 -= 1
            else:
                nums1[i] = nums2[pointer_2]
                pointer_2 -= 1
```