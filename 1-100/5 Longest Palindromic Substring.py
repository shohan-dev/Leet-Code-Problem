class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        s = '#' + '#'.join(s) + '#'
        n = len(s)
        p = [0] * n
        c = r = 0
        max_len = 0
        center_index = 0

        for i in range(n):
            mirror = 2 * c - i
            if i < r:
                p[i] = min(r - i, p[mirror])
            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and s[i + p[i] + 1] == s[i - p[i] - 1]:
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]
            if p[i] > max_len:
                max_len = p[i]
                center_index = i

        start = (center_index - max_len) // 2
        return s[center_index - max_len:center_index + max_len + 1].replace('#', '')
