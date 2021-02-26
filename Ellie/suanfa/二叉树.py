class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    count = 0
    nodeVal = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.dfs(root, k)
        return self.nodeVal

    def dfs(self, node, k):

        if node != None:
            self.dfs(node.left, k)
            self.count = self.count + 1
        if self.count == k:
            self.nodeVal = node.val
            # 将该节点的左右子树置为 None,来结束递归，减少时间复杂度
            node.left = None
            node.right = None
            self.dfs(node.right, k)
