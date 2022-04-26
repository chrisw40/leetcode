class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n <= 0:
            return []
        return self.allPossibleFBTRecursive({}, n)
    
    def allPossibleFBTRecursive(self, map, n):
        if n in map:
            return map[n]
        
        result = []
        
        if n == 0:
            return result
        
        if n == 1:
            root = TreeNode(0)
            return [root]

        for i in range(1, n+1):
            leftSubtrees = self.allPossibleFBTRecursive(map, i - 1)
            rightSubtrees = self.allPossibleFBTRecursive(map, n - i)
            for leftTree in leftSubtrees:
                for rightTree in rightSubtrees:
                    root = TreeNode(0)
                    root.left = leftTree
                    root.right = rightTree
                    result.append(root)
                    
        map[n] = result
        return result