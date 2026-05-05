class Solution:
    def numTrees(self, n: int) -> int:
        # Initialize a list to store the number of unique BSTs for each number of nodes.
        # trees[i] will hold the number of unique BSTs that can be formed with i nodes.
        # Base case: trees[0] = 1 (empty tree), trees[1] = 1 (single node tree)
        trees = [1] * (n + 1)

        for node in range(2, n + 1):
            total = 0
            # For each number i from 1 to node, consider i as root
            for root in range(1, node + 1):
                # The number of unique BSTs with `root` as root is the number of
                # left subtrees (root - 1 nodes) * number of right subtrees (node - root nodes)
                total += trees[root - 1] * trees[node - root]
            trees[node] = total

        # Return the number of unique BSTs that can be formed with `n` nodes
        return trees[n]
