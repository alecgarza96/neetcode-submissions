# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)

        return root
    
    def traverse(self, root: Optional[TreeNode]):
        if root:
            print(root.val)
            #if left and right, swap
            if root.left and root.right:
                tempLeft = root.left
                tempRight = root.right
                root.right = tempLeft
                root.left = tempRight
            elif root.left and not root.right:
                #populate root.right with null, then swap
                tempLeft = root.left
                root.right = tempLeft
                root.left = None
            else:
                tempRight = root.right
                root.left = tempRight
                root.right = None
            self.traverse(root.left)
            self.traverse(root.right)

        