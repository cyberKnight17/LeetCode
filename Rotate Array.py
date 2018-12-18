class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = 0
        while n < k:
            nums.insert(0, nums[-1])
            del nums[-1]
            n = n + 1
        return nums


test_instance = Solution()

print(test_instance.rotate([1, 2, 3, 4, 5,6,7], 3))
print(test_instance.rotate([-1, -100, 3, 99], 2))