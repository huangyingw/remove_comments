class Solution(object):
    def increasingBST(self, root, tail=None):
        if root is None:
            return tail
        copy_root = TreeNode(root.val)
        copy_root.right = self.increasingBST(root.right, tail)
        return self.increasingBST(root.left, copy_root)
