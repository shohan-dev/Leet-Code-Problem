class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        minus = 0
        if s== "":
            return 0
        if len(s)==1 and not s[0].isdigit():
            return 0
        if s[0] == "-" or s[0] == "+":
            minus = 1
        end = len(s)

        if not s[minus:].isdigit():
            end = [not x.isdigit() for x in s[minus:] ].index(True)

        if not s[minus].isdigit():
            res = 0
        else:
            res = int(s[minus:end+minus])
            
        if s[0]=="-":
            res *= -1
        if res> 2**31 - 1:
            res = 2**31 - 1
        elif res< -2**31:
            res = -2**31

        return res