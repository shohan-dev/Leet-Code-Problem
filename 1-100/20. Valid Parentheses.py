class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','{':'}','[':']'}
        l=[]
        for p in s:
            if not l and p in d.values():
                return False
            elif p in d.keys():
                l.append(p)
            elif p == d[l[-1]]:
                l.pop()
            else:
                return False

        if not l:
           return True
        else:
           return False