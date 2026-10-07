class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        res,curr,count,i = 1,nums[0],0,0
        while i<len(nums):
            if nums[i]!=curr:
                curr = nums[i]
                count= 1
                i+=1
                curr+=1
            else:
                i+=1
                count+=1
                curr+=1
            res = max(res,count)
        return res
