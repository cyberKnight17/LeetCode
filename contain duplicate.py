class Solution:
    def containsDuplicate(self, nums: list):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_length = len(nums)

        if nums_length == len(set(nums)):
            return False

        else:
            nums_sorted = sorted(nums)
            for i in range(0, nums_length - 1):
                if nums_sorted[i] == nums_sorted[i+1]:
                    return True
