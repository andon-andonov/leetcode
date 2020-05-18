class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        if len(nums) == 0:
            return 0
        newlen = 1;
        curr_val = nums[0];
        for _, val in enumerate(nums, 1):
            if curr_val != val:
                curr_val = val
                nums[newlen] = val
                newlen += 1
        return newlen
        
