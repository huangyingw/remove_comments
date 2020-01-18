class Solution(object):
    def isValidBST(self, root):
        if not root:
	        return True
        stack, result = [], []
        while stack or root:
        	if root:
        		stack.append(root)
          root = root.left
         else:
        		root = stack.pop()
          result.append(root.val)
          root = root.right
        previous = result[0]
        for index in range(1, len(result)):
        	if previous >= result[index]:
        		return False
         previous = result[index]
        return True
