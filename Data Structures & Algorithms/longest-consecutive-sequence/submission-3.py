class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        #OPTION 1 - Using Sorted Array    
        # nums = sorted(set(nums))
        # res = 1
        # count = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1] + 1:
        #         count += 1
        #     else:
        #         count = 1
        #     res = max(res, count)

        # return res

        #OPTION 2 - Using Set
        longest = 0
        seen = set(nums)
        for num in nums:
            if num - 1 not in seen:
                length = 1
                while (num+length) in seen:
                    length+=1
                longest = max(length,longest)
        return longest
                
        
