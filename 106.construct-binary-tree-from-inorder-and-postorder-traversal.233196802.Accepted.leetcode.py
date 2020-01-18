class Solution(object):
    def buildTree(self, inorder, postorder):
        self.index = len(inorder) - 1

        def recursive(postorder, inorder, start, end):
        	if start > end:
        		return None
         node = TreeNode(postorder[self.index])
         self.index -= 1
         if start == end:
        		return node
         search_index = 0
         for i in range(start, end+1):
        		if inorder[i] == node.val:
        			search_index = i
           break
         node.right = recursive(postorder, inorder, search_index+1, end)
         node.left = recursive(postorder, inorder, start, search_index-1)
         return node
        return recursive(postorder, inorder, 0, len(inorder)-1)
