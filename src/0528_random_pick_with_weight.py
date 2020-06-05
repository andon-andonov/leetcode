import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        w_sum = sum(w)
        self.r = [0] * len(w)
        self.r[0] = w[0] / w_sum
        for index, item in enumerate(w[1:], start=1):
            self.r[index] = self.r[index-1] + w[index] / w_sum

    def pickIndex(self) -> int:
        rand_val = random.random()
        index = bisect.bisect_left(self.r, rand_val)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
