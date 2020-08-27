#!/usr/bin/env python
# -*- coding: utf-8 -*-

class solution(object):

    '最长公共连续子序列'
    #时间：O（N2) 空间：O(m*n)
    def lcs(self, arr1, arr2):
        m, n = len(arr1), len(arr2)
        dp = [[0]*n for _ in range(m)]  #n列m行
        max_length = 0
        for i in range(m):
            for j in range(n):
                if arr1[i] == arr2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                if  dp[i][j] > max_length :
                    max_length = dp[i][j]
        return max_length
    
    '最长公共子序列'
    def lcs(arr1, arr2):
        m, n = len(arr1), len(arr2)
        dp = [[0]*n for _ in range(m)]  #n列m行
        max_length = 0
        for i in range(m):
            for j in range(n):
                if arr1[i] == arr2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) #子问题最大解
                if  dp[i][j] > max_length :
                    max_length = dp[i][j
        return max_length

    '最长递增子序列'
    def lis(arr):
        temp = []
        temp.append(arr[0])
        for i in range(len(arr)):
            if arr[i] > temp[-1]:
                temp.append(arr[i])
            else:
                idx = binaryfind(temp, arr[i])
                temp[idx] = arr[i]
        return len(temp)

    def binaryfind(arr, target):
        hi = len(arr) -1
        lo = 0
        while hi >= lo:
            pivot = int(lo + (hi-lo)/2)
            if arr[pivot] < target:
                lo = pivot + 1
            elif arr[pivot] > target:
                hi = pivot - 1
            else:
                return pivot
        return lo
    
    '连续子序列的最大和'
    def lis(arr):
        m = len(arr)
        dp = [arr[0]] + [0]*(m-1)
        for i in range(1, m):
            if dp[i-1] >= 0:
                dp[i] = dp[i-1] + arr[i]
            else:
                dp[i] = arr[i]
        return max(dp)

if __name__ == '__main__':
    
    s1 = "'abccdefg"
    s2 = "abd"
    
    print('最长公共连续子序列长度：', lcs(s1,s2))


