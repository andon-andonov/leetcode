class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        if n < 3:
            return True
        div, mod = divmod(n, 2)
        if mod:
            return False
        else:
            return self.isPowerOfTwo(div)
