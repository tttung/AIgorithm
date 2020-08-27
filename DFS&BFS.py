#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    'BFS'
    '从上到下打印二叉树'
    def levelOrder(self, root):
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res
            
    '从上到下打印二叉树，每一层输出一行'
    def levelOrder(self, root):
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res

    '从上到下之字形打印二叉树'
    def levelOrder(self, root):
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2: tmp.appendleft(node.val) # 偶数层 -> 队列头部
                else: tmp.append(node.val) # 奇数层 -> 队列尾部
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
                res.append(list(tmp))
            return res

    '到离它最近的陆地的距离最大的海洋'
    def maxDistance(self, grid: List[List[int]]) -> int:
        res = 0
        q = []
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append([i,j,0])
        print(q)
        while q:
            fr = q.pop(0)
            res = max(res, fr[2])
            for i in directions:
                x = fr[0] + i[0]
                y = fr[1] + i[1]
                if x<m and x>=0 and y<n and y>=0 and grid[x][y]==0:
                    q.append([x,y,fr[2]+1])
                    grid[x][y] = 1

        return -1 if res==0 else res
            
    'DFS'
    '岛屿的最大面积'
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 1:
            return 0    #调用加0
        grid[i][j] = 0
        return 1 + dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j-1) + dfs(grid, i, j+1) #每次调用+1

    def maxAreaOfIsland(self, grid):
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans

    '岛屿数量'
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 1:
            return 0 #调用加0
        grid[i][j] = 0
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]: （决定层中深度搜索的方向顺序）
            next_i, next_j = i + di, j + dj
            self.dfs(grid, next_i, next_j)
        return 1

    def IslandCount(self, grid):
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans += self.dfs(grid, i, j)
        return ans

if __name__ == '__main__':

