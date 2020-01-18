class Solution(object):
    def recoverTree(self, root):
        first, second, prev = None, None, None

        def inorder(root):
        	if root:
        		inorder(root.left)
          if prev is not None and root.val < prev.val:
        			if first is None:
        				first = root
           else:
        				second = root
          prev = root
          inorder(root.right)
        inorder(root)
        if first and second:
        	first.val, second.val = second.val, first.val
