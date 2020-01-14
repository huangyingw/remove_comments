class Solution(object):
    def allPossibleFBT(self, N):
        memo = {}
        def helper(n):
            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode(0)]
            if n in memo:
                return memo[n]
            result = []
            for left_size in range(1, n, 2):
                right_size = n - 1 - left_size
                left_subtrees = helper(left_size)
                right_subtrees = helper(right_size)
                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        root = TreeNode(0)
                        root.left = left_subtree
                        root.right = right_subtree
                        result.append(root)
            memo[n] = result
            return result
        return helper(N)
