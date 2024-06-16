class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        q = deque()
        for c in s:
            if c in q:
                while q.popleft() != c:
                    pass
            q.append(c)
            res = max(res, len(q))
        return res