class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        # Creating a dictionary where the value is stored a key and index as value
        for index,value in enumerate(nums):
            result[value] = index

        for i,n in enumerate(nums):
            diff = target - n
        # Check if the diff is in result and diff's index is not i since  
            if diff in result and result[diff] != i:
                return [i,result[diff]]
        return[]
        

        