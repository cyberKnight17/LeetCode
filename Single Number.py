class Solution:
    def singleNumber(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]


s1 = Solution()
print(s1.singleNumber([1, 1, 2, 2, 5]))