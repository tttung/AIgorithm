#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    
    '快速排序'
    def partition(self, arr, start, end):
        '找轴点应该在的位置，左侧比他小，右侧比他大'
        low = start
        high = end
        pivot = arr[start]   #选定轴点，‘坑’
        while low < high:    #直到访问完所有元素
            while low < high and arr[high] >= pivot:  #右指针元素大于轴点
                high -= 1                             #右指针左移
            arr[low] = arr[high]                      #右指针元素小于轴点，将其入坑；此时high位置为新坑
            #目前右边的都比轴点大
            while low <high and arr[low] < pivot:     #左指针元素小于轴点
                low += 1                              #左指针右移
            arr[high] = arr[low]                      #左指针元素大于轴点，将其入新坑high；此时low为新新坑
            #目前左边的都比轴点小
        arr[low] = pivot                              #轴点位置'坑'确定，一轮结束
        return low
            
    def quick_sort(self, arr, left, right):
        if left < right:
            temp = self.partition(arr, left, right)      #轴点位置
            self.quick_sort(arr, left, temp - 1)
            self.quick_sort(arr, temp + 1, right)
            return arr

    'TopK 基于快速排序partition方法'
    def getLeastNumbers(self, arr, k):
        if k > len(arr) or k <= 0:
            return []
        start = 0
        end = len(arr) - 1
        index = self.partition(arr, start, end)
        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.partition(arr, start, end)
            if index < k-1:
                start = index + 1
                index = self.partition(arr, start, end)
        return arr[:k]



    '归并排序'
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

    def MergeSort(self, lists):
        if len(lists) <= 1:
            return lists
        middle = int(len(lists)/2)
        left = self.MergeSort(lists[:middle])
        right = self.MergeSort(lists[middle:])
        return self.merge(left, right)

    '堆排序'
    def heap_adjust(self, A,i,size):
        left = 2*i+1
        right = 2*i+2
        max_index = i
        if left < size and A[left] > A[max_index] :
            max_index = left
        if right < size and A[right] > A[max_index]:
            max_index = right
        if max_index != i:
            temp = A[i]
            A[i] =A[max_index]
            A[max_index] = temp
            self.heap_adjust(A,max_index,size) #以替换的点为父节点，再调整所在的堆

    def build_heap(self, A,size):
        for i in range(size//2,-1,-1):
            self.heap_adjust(A,i,size)

    def heap_sort(self, A):
        size = len(A)
        self.build_heap(A,size) #初始化堆
        for i in range(len(A)-1,0,-1):
            temp = A[i]
            A[i] = A[0]
            A[0] = temp         #将最大元素置于数组后的位置
            self.heap_adjust(A,0,i)
        return A

if __name__ == '__main__':
    nums = [3,2,5,4,6,9,11,33,22]
    test = Solution()
    res = test.quick_sort(nums, 0, len(nums)-1)
    res = test.MergeSort(nums)
    res = test.heap_sort(nums)
    print('sorted nums is:', res)
