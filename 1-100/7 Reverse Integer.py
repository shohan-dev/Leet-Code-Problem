class Solution:
    def reverse(self, x: int) -> int:
        a=str(x)
        if a[0]=="-":
            b=a[1:]
            c='-'+b[::-1]
            c=int(c)
            if c > 2**31:
                return 0
            if c < -2**31:
                return 0
            else:
                return c
        else:
            b=a[::-1]
            b=int(b)
            if b > 2**31 :
                return 0
            if b < -2**31 :
                return 0
            else:
                return b

