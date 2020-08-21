#!/usr/bin/env python
# -*- coding: utf-8 -*-

'最长公共连续子序列'
#时间：O（N2) 空间：O(m*n)
def lcs(arr1, arr2):
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


if __name__ == '__main__':
    
    s1 = "'abccdefg"
    s2 = "abd"
    
    print('最长公共连续子序列长度：', lcs(s1,s2))


