class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        queue = deque()
        queue.append(("", 0, 0))
        while queue:
            parenthesisString, openCount, closeCount = queue.popleft()
            if openCount == n and closeCount == n:
                result.append(parenthesisString)
            else:
                if openCount < n:
                    queue.append((parenthesisString + "(", openCount + 1, closeCount))
            
                if openCount > closeCount:
                    queue.append((parenthesisString + ")", openCount, closeCount + 1))
                
        return result
    

#         result = []
#         parenthesisString = [0 for x in range(2*n)]
#         self.generateParenthesisRecursive(n, 0, 0, parenthesisString, 0, result)
#         return result
    
#     def generateParenthesisRecursive(self, n, openCount, closeCount, parenthesisString, index, result):
#         if openCount == n and closeCount == n:
#             result.append(''.join(parenthesisString))
#         else:
#             if openCount < n:
#                 parenthesisString[index] = "("
#                 self.generateParenthesisRecursive(n, openCount + 1, closeCount, parenthesisString, index + 1, result)
                
#             if openCount > closeCount:
#                 parenthesisString[index] = ")"
#                 self.generateParenthesisRecursive(n, openCount, closeCount + 1, parenthesisString, index + 1, result)