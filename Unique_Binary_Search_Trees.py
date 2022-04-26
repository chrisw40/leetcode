class Solution:
    def numTrees(self, n: int) -> int:
#         if n <= 0:
#             return 1
#         count = 0
#         for i in range(1, n+1):
#             countOfLeftSubtrees = self.numTrees(i - 1)
#             countOfRightSubtrees = self.numTrees(n - i)
#             count += (countOfLeftSubtrees * countOfRightSubtrees)
            
#         return count


        return self.numTreesRecursive({}, n)


    def numTreesRecursive(self, map, n):
        if n in map:
            return map[n]
        
        if n <= 1:
            return 1
        count = 0
        for i in range(1, n+1):
            countOfLeftSubtrees = self.numTreesRecursive(map, i - 1)
            countOfRightSubtrees = self.numTreesRecursive(map, n - i)
            count += (countOfLeftSubtrees * countOfRightSubtrees)
            
        map[n] = count
        return count