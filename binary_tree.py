# -------------------- Binary Tree - DFS --------------------
#Depth-First Search - When you recurse, you keep going deeper before coming back up

# 104. Maximum Depth of Binary Tree
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

# 872. Leaf-Similar Trees
# Method 1
class Solution(object):
    def leafSimilar(self, root1, root2):
        self.res1 = []
        self.res2 = []

        def helper1(node1):
            if not node1: return
            if node1:
                helper1(node1.left)
                helper1(node1.right)
                if not node1.left and not node1.right:
                    self.res1.append(node1.val)

        def helper2(node2):
            if not node2: return
            if node2:
                helper2(node2.left)
                helper2(node2.right)
                if not node2.left and not node2.right:
                    self.res2.append(node2.val)
        
        helper1(root1)
        helper2(root2)
        return self.res1 == self.res2

# Method 2: 
class Solution(object):
    def leafSimilar(self, root1, root2):
        def get_leaves(node):
            res = []
            def dfs(n):
                if not n: return
                dfs(n.left)
                dfs(n.right)
                if not n.left and not n.right: res.append(n.val)
            dfs(node)
            return res
        return get_leaves(root1) == get_leaves(root2)
    
# Method 3:
class Solution(object):
    def leafSimilar(self, root1, root2):  
        def get_leaves(node):
            if not node: return []
            if not node.left and not node.right: return [node.val]
            return get_leaves(node.left) + get_leaves(node.right)
        return get_leaves(root1) == get_leaves(root2)

# 1448. Count Good Nodes in Binary Tree
class Solution(object):
    def goodNodes(self, root):
        if not root: return 0
        self.cnt = 0
        def helper(node, num):
            if not node: return
            if node.val >= num:
                self.cnt += 1
                num = node.val
            helper(node.left, num)
            helper(node.right, num)
        helper(root, root.val)
        return self.cnt


# 437. Path Sum III
class Solution(object):
    def pathSum(self, root, targetSum):
        if not root: return 0
        def count_paths(node, curSum):
            if not node: return 0
            path_cnt = 1 if node.val == curSum else 0
            path_cnt += count_paths(node.left, curSum - node.val)
            path_cnt += count_paths(node.right, curSum - node.val)
            return path_cnt
        def dfs(node): # treat each node as a starts
            if not node: return 0
            total_paths = count_paths(node, targetSum) # count all valid paths starting at this node
            total_paths += dfs(node.left) # recursively do the same for every node
            total_paths += dfs(node.right)
            return total_paths
        return dfs(root)


# 1372. Longest ZigZag Path in a Binary Tree
class Solution(object):
    def longestZigZag(self, root):
        self.res = 0
        def dfs(node, leftLen, rightLen):
            if not node: return  
            self.res = max(self.res, leftLen, rightLen)
            dfs(node.left, rightLen+1, 0)
            dfs(node.right, 0, leftLen+1)
        dfs(root, 0, 0)
        return self.res

# 236. Lowest Common Ancestor of a Binary Tree
def lowestCommonAncestor(self, root, p, q):
    if not root: return None
    if root in [p,q]: return root
    l = self.lowestCommonAncestor(root.left, p, q)
    r = self.lowestCommonAncestor(root.right, p, q)

    if l and r: return root
    return l or r


# -------------------- Binary Tree - BFS --------------------
# BFS processes nodes level by level using a queue
# 199. Binary Tree Right Side View
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        res = []
        if not root: return []
        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1: res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res


# 1161. Maximum Level Sum of a Binary Tree
# Method 1 - BFS
def maxLevelSum(self, root):
    if not root: return 0

    s = float("-inf")
    level = 1
    res = 1
    
    queue = deque([root])

    while queue:
        n = len(queue)
        level_s = 0
        for i in range(n):
            node = queue.popleft()
            level_s = level_s + node.val
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        if level_s > s: 
            s = level_s
            res = level
        level += 1
    return res


# Method 2 - DFS
def maxLevelSum(self, root):
    levelSum = {}
    def dfs(node, level):
        if not node: return 0
        if level in levelSum: levelSum[level] += node.val
        else: levelSum[level] = node.val

        dfs(node.left, level+1)
        dfs(node.right, level+1)

    dfs(root, 1)
    return max(levelSum, key=lambda x: (levelSum(x), -x)) # pick the level with the highest sum
        # levelSum = levelSum.key(); -x: if tie -> pick the smallest level number

# -------------------- Binary Search Tree - BST --------------------
# 700. Search in a Binary Search Tree
def searchBST(self, root, val):
    if not root: return None
    if root.val == val: return root
    elif root.val > val: return self.searchBST(root.left, val)
    else: return self.searchBST(root.right, val)

# 450. Delete Node in a BST
def deleteNode(self, root, key):
    if not root: return None
    if root.val > key: root.left = self.deleteNode(root.left, key)
    elif root.val < key: root.right = self.deleteNode(root.right, key)
    else:
        if not root.right: return root.left 
        if not root.left: return root.right
        if root.left and root.right: 
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)
    return root




                
