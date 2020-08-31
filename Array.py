#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    '合并两个有序数组'
    def merge(self, nums1, m, nums2, n):
        
        # Make a copy of nums1.
        nums1_copy = nums1[:m]
        nums1[:] = []
        
        # Two get pointers for nums1_copy and nums2.
        p1 = 0
        p2 = 0
        
        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        
        # if there are still elements to add
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

    '旋转数组最小值'
    def minArray(self, numbers):
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]


if __name__ == '__main__':
    test = Solution()

