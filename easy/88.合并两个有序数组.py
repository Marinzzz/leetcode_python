class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        if not nums1:
            return nums2
        pointer_1 = m - 1
        pointer_2 = n - 1
        for i in range(m + n - 1, -1, -1):
            if pointer_2 < 0:
                nums1[i] = nums1[pointer_1]
                pointer_1 -= 1
            elif pointer_1 < 0:
                nums1[i] = nums2[pointer_2]
                pointer_2 -= 1
            elif nums1[pointer_1] > nums2[pointer_2]:
                nums1[i] = nums1[pointer_1]
                pointer_1 -= 1
            else:
                nums1[i] = nums2[pointer_2]
                pointer_2 -= 1