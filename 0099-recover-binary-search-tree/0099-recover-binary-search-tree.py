# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: Optional[TreeNode], arr: List[int]) -> List[int]:
        if root == None:
            return arr
        
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)

    def inorder_fix(self, root: Optional[TreeNode], v1: int, v2: int) -> None:
        if root == None:
            return 
        if root.val == v1:
            root.val = v2
        elif root.val == v2:
            root.val = v1
        self.inorder_fix(root.left, v1, v2)
        self.inorder_fix(root.right,v1,v2)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        arr = []
        self.inorder(root, arr)
        sorted_arr = sorted(arr)
        v1 = None
        v2 = None
        for i in range(0, len(arr)):
            if arr[i] != sorted_arr[i]:
                if v1 == None:
                    v1 = arr[i]
                else:
                    v2 = arr[i]

        self.inorder_fix(root,v1, v2)

        