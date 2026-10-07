class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        numset = set(nums)

        for num in numset:
            if num-1 not in numset:
                current = num
                length = 1
                while current+1 in numset:
                    current+=1
                    length+=1
                longest = max(length,longest)
        return longest



            

        