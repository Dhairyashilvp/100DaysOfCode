class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # print(root)
        if root == None:
            return 0
        lst = self.maxDepth(root.left)
        rst = self.maxDepth(root.right)
        md = max(lst,rst)+1
        return md