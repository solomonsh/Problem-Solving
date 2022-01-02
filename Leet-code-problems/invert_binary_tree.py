# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if root == None:
            return None
        queue = deque()
        queue.append(root)

        while queue:
            current = queue.popleft()
            if current.left != None:
                queue.append(current.left) 
            if current.right != None:
                queue.append(current.right)

            temp = current.left

            current.left = current.right
            current.right = temp
       
        return root

 
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

sol = Solution()


# for testing 
# queue = deque()
# queue.append(sol.invertTree(root))

# while queue:
#     current = queue.popleft()
#     if current.left != None:
#             queue.append(current.left) 
#     if current.right != None:
#             queue.append(current.right)
#     print(current.val)
    
