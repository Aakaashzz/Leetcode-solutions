# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        l=defaultdict(list)
        def traversal(root,h):
            if root is None:
                return
            l[h].append(root.val)
            traversal(root.left,h+1)
            traversal(root.right,h+1)
        traversal(root,0)
        res=[]
        for i in l.values():
            res.append(max(i))
        return res