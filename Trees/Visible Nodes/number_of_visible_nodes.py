from collections import deque
class TreeNode:

    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def visible_nodes(root):
    if not root:
        return 0
    queue = deque()
    queue.append(root)
    left_visibles = []
    while queue:
        n = len(queue)
        for i in range(n):
            current = queue.popleft()
            if i == 0:
                left_visibles.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return len(left_visibles)



root_1 = TreeNode(8)
root_1.left = TreeNode(3)
root_1.right = TreeNode(10)

root_1.left.left = TreeNode(1)
root_1.left.right = TreeNode(6)

root_1.left.right.left = TreeNode(4)
root_1.left.right.right = TreeNode(7)

root_1.right.right = TreeNode(14)
root_1.right.right.left = TreeNode(13)


print(visible_nodes(root_1))