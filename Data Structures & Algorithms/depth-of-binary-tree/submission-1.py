# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        need a way to track maximum depth
        need a way to compare maximum depth to current depth
        recursively crawl each branch of the tree
        """

        if not root:
            return 0
        
        def countDepth(current, ans, root):
            if root:
                print(root.val)
                print(current)
                print(str(ans)+"\n")
                if current >= ans:
                    ans = current
                return 1 + max(countDepth(current, ans, root.left), countDepth(current, ans, root.right))
            return ans
        

        return countDepth(0, 0, root)


