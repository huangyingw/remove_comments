class Solution(object):
    def constructFromPrePost(self, pre, post):
        def helper(pre_start, pre_end, post_start, post_end):
            if pre_start == pre_end:
                return None
            root = TreeNode(pre[pre_start])
            if post_end == post_start + 1:
                return root
            idx = pre_indices[post[post_end - 2]]
            left_size = idx - pre_start - 1
            root.left = helper(pre_start + 1, idx, post_start, post_start + left_size)
            root.right = helper(idx, pre_end, post_start + left_size, post_end - 1)
            return root
        pre_indices = {val: i for i, val in enumerate(pre)}
        return helper(0, len(pre), 0, len(post))
