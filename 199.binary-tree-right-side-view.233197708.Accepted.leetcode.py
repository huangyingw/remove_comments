class Solution(object):
    def rightSideView(self, root):
        if not root:
        	return []
        stack, node_depth = [(root, 0)], {}
        while stack:
        	node, depth = stack.pop(0)
         if depth not in node_depth:
        		node_depth[depth] = node.val
         if node.right:
        		stack.append((node.right, depth+1))
         if node.left:
        		stack.append((node.left, depth+1))
        return node_depth.values()
