"""314. Binary Tree Vertical Order Traversal"""
from collections import defaultdict, deque

""" Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]
            1  2 3 4
1              3
              /\
             /  \
2            9  20
                /\
               /  \
3             15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]

Workflow Timestamps
1. Make Sure You Understand the Problem

Ex1: root = 5
o/p:[5]

Ex2: root = 5
           / \
          1   2
o/p: [[1],[5],[2]]

Ex3: root = 5
           / \
          1   2
         /\   /\
        3  4 2  6
        
o/p: [[3],[1],[5,4,2],[2],[6]]

2. Design and Verify a Solution

-           5 col = 0
           / \
 col=-1   1   2 col = 1
         /\   /\
 col=-2 3  4 2  6  col = 2
 
 - We need a dictionary to store the cols and the values as list 
 - Traverse the tree and add the values to the dictionary using a queue
 - We can go through the dictionary values and add them to the res by sorting the dictinary 
 
 Time Complexity: O(nlogn)
 Space Complexity: O(n)
3. Write the Code And Pass Test Cases.
"""


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution Class"""

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        For each left and right subtree, we can keep track of the columns in a queue and store the
        subtree values in the dictionary with the column as index and then return the values from the
        sorted dictionary
        """

        col_dict = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            root, cur_col = queue.popleft()

            col_dict[cur_col].append(root.val)
            if root.left:
                queue.append((root.left, cur_col-1))
            if root.right:
                queue.append((root.right, cur_col+1))

        return [val for _,val in sorted(col_dict.items())]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print(s.verticalOrder(root))

