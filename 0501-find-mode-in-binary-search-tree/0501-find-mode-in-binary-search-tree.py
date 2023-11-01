# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict = {}

        def traversal(node):
            nonlocal dict
            if not node: return 
            if node.val in dict: dict[node.val] = dict[node.val] + 1
            else: dict[node.val] = 1
            traversal(node.left)
            traversal(node.right)
            return

        traversal(root)

        answer = []

        sortDict = sorted(dict.items(), key = lambda x:x[1])

        compare = float('-inf')

        for i in range(len(sortDict) - 1, -1, -1):
            if sortDict[i][1] >= compare:
                answer.append(sortDict[i][0])
                compare = sortDict[i][1]
            else: break

        return answer