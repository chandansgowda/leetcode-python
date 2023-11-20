"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        d = 1
        if root.children:
            d += max(self.maxDepth(child) for child in root.children)
        return d
        
