# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build_trees(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]

            all_trees = []
            for root_val in range(start, end + 1):
                # Recursively build all possible left and right subtrees
                left_subtrees = build_trees(start, root_val - 1)
                right_subtrees = build_trees(root_val + 1, end)

                # Combine them with the current root
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        all_trees.append(root)

            return all_trees

        return build_trees(1, n)
