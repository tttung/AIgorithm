#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    '合并两个有序数组'
    def merge(self, a, b):
        c = []
        h = j = 0
        while j < len(a) and h < len(b):
            if a[j] < b[h]:
                c.append(a[j])
                j += 1
            else:
                c.append(b[h])
                h += 1
        if j == len(a):
            for i in b[h:]:
                c.append(i)
        else:
            for i in a[j:]:
                c.append(i)
        return c

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
    nums = [4, 5, 6, 1, 2, 3]
    test = Solution()
    res = test.minArray(nums)
    print('res is', res)
