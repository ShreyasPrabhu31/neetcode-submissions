# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndxMap = {val : i for i, val in enumerate(inorder)}

        def buildSubtree(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None
            
            rootVal = preorder[preLeft]
            root = TreeNode(rootVal)
            inorderRootIndx = inorderIndxMap[rootVal]
            leftSubtreeSize = inorderRootIndx - inLeft
            root.left = buildSubtree(preLeft + 1, preLeft + leftSubtreeSize, inLeft, inorderRootIndx - 1)
            root.right = buildSubtree(preLeft + leftSubtreeSize + 1, preRight, inorderRootIndx + 1, inRight)

            return root
        return buildSubtree(0, len(preorder) - 1, 0, len(inorder) - 1)
