class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        wordLen = len(word)
        result = []
        queue = deque()
        queue.append((list(), 0, 0))
        while queue:
            abWord, start, count = queue.popleft()
            if start == len(word):
                if count != 0:
                    abWord.append(str(count))
                result.append(''.join(abWord))
            else:
                queue.append((list(abWord), start + 1, count + 1))

                if count != 0:
                    abWord.append(str(count))

                newWord = list(abWord)
                newWord.append(word[start])
                queue.append((newWord, start + 1, 0))

        return result


#         result = []
#         self.generateAbbreviationsRecursive(word, list(), 0, 0, result)
#         return result

#     def generateAbbreviationsRecursive(self, word, abWord, start, count, result):
#         if start == len(word):
#             if count != 0:
#                 abWord.append(str(count))
#             result.append(''.join(abWord))
#         else:
#             self.generateAbbreviationsRecursive(word, list(abWord), start + 1, count + 1, result)

#             if count != 0:
#                 abWord.append(str(count))
                
#             newWord = list(abWord)
#             newWord.append(word[start])
#             self.generateAbbreviationsRecursive(word, newWord, start + 1, 0, result)