class Solution(object):
    def kthSmallest(self, root, k):
        if not root:
        	return 0
        stack = [root]
        count, curr = 0, root
        while stack:
        	if curr.left:
        		stack.append(curr.left)
          curr = curr.left
         else:
        		val = stack.pop()
          count += 1
          if count == k:
        			return val.val
          if val.right:
        			stack.append(val.right)
           curr = val.right
        return float('-inf')
