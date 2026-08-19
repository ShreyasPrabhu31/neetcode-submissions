# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val : i for i, val in enumerate(inorder)}

        def buildSubtree(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None
            
            root_val = preorder[preLeft]
            root = TreeNode(root_val)
            inorder_root_index = inorder_index_map[root_val]
            left_subtree_size = inorder_root_index - inLeft
            root.left = buildSubtree(preLeft + 1, preLeft + left_subtree_size, inLeft, 
                                    inorder_root_index - 1)
            root.right = buildSubtree(preLeft + left_subtree_size + 1, preRight, 
                                    inorder_root_index + 1, inRight)

            return root
        
        return buildSubtree(0, len(preorder) - 1, 0, len(inorder) - 1)