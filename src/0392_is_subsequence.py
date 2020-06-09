class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for ch in s:
            try:
                i = t.index(ch, start)
                start = i + 1
            except ValueError:
                return False
        return True
