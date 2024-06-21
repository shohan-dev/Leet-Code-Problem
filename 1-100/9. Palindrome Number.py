class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = str(x)
        return res[::1] == res[::-1]
        