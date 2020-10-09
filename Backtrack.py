#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    '组合项'
    def combine(self, n, k):
        res = []
        path = []
        self.dfsHelper(n, k, 1, path, res)
        return res

    def dfsHelper(self, n, k, level, path, res):
        if len(path) == k:
            res.append(path)
            return
        for i in range(level, n):
            path.append(i)
            self.dfsHelper(n, k, i+1, out, res)
            path.pop()

    '全排列'
    def permute(self, num):
        res = []
        out = []
        visted = {}
        self.permuteDFS(num, visted, out, res)
        return res
    def permuteDFS(self, num, visted, out, res):
        if len(out) = len(num):
            res.append(out)
            return
        for i in range(len(num)):
            if visted[i] == 1: continue
            visted[i] = 1
            out.append(num[i])
            self.permuteDFS(num, visted, out, res)
            out.pop()
            visted[i] = 0

    '子集'
    def subsets(self, S):
        res = []
        out = []
        sort(S)
        self.getSubsets(S, 0, out, res)
        return res
    def getSubsets(self, S, pos, out, res):
        res.append(out)
        for i in range(pos, len(S)):
            res.append(out)
            self.getSubsets(S, i+1, out, res)
            out.pop()

    '组合之和 每个数字可重复'
    def combineSum(self, candidates, target):
        res = []
        out = []
        self.combineSumDFS(candidates, target, 1, out, res)
        return res
    
    def combineSumDFS(self, candidates, target, start, out, res):
        if target < 0: return
        if target == 0: res.append(out)
        for i in range(start, len(candidates)):
            out.append(candidates[i])
            self.combineSumDFS(candidates, target - candidates, i, out, res)
            out.pop()

    '组合之和 每个数字不可重复'
    def combineSum2(self, candidates, target):
        res = []
        out = []
        self.combineSumDFS2(candidates, target, 1, out, res)
        return res

    def combineSumDFS2(self, candidates, target, start, out, res):
        if target < 0: return
        if target == 0: res.append(out)
        for i in range(start, len(candidates)):
            out.append(candidates[i])
            self.combineSumDFS2(candidates, target - candidates, i+1, out, res)
            out.pop()

    '组合之和 k个数、不可重复'
    def combineSum3(self, candidates, target, k):
        res = []
        out = []
        self.combineSum3DFS(candidates, target, 1, out, res, k)
        return res
    
    def combineSumDFS3(self, candidates, target, start, out, res, k):
        if target < 0: return
        if target == 0 and len(out)== k: res.append(out)
        for i in range(start, len(candidates)):
            out.append(candidates[i])
            self.combineSum3DFS(candidates, target - candidates, i+1, out, res, k)
            out.pop()

    '二叉树中和为某一值的路径'
    def pathSum(self, root, sum):
        res = []
        out = []
        self.helper(root, sum, out, res)
        return res
    
    def helper(self, root, sum, out, res):
        if not root: return
        out.append(root.val)
        if sum - root.val == 0 and not root.left and not root.right:
            res.append(out)
        self.helper(root.left, sum - root.val, out, res)
        self.helper(root.right, sum - root.val, out, res)
        out.pop()
            
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return Ture
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    'N皇后'
    def NQueens():

if __name__ == '__main__':
    test = Solution()
