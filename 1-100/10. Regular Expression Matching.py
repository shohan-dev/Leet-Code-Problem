class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def backtrack(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == -1:
                result = i == -1
            elif i == -1:
                result = j > 0 and p[j] == '*' and backtrack(i, j - 2)
            elif p[j] == '*':
                result = (backtrack(i, j - 2) or
                          (p[j - 1] == s[i] or p[j - 1] == '.') and backtrack(i - 1, j))
            else:
                result = (p[j] == '.' or s[i] == p[j]) and backtrack(i - 1, j - 1)

            memo[(i, j)] = result
            return result

        return backtrack(len(s) - 1, len(p) - 1)