class Solution(object):
    def maxPathSum(self, root):
        self.result = float('-inf')
        self.dfs(root)
        return self.result

    def dfs(self, root):
    	if not root:
    		return 0
     l = self.dfs(root.left)
     r = self.dfs(root.right)
     max_one_end = max(max(l, r)+root.val, root.val)
     max_path = max(max_one_end, l+r+root.val)
     self.result = max(self.result, max_path)
     return max_one_end
