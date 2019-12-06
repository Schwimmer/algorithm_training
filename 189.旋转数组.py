#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        k有可能超过int的长度
        """

        """ 第一版，超出时间限制，时间复杂度O(kn)
        k = k % len(nums)
        for i in range(k):
            temp = nums[-1]
            for j in range(len(nums)-1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = temp
        """

        """ 
        第二版，通过三次反转的形式，时间复杂度O(n)
        因为旋转之后，总是后面的在头部，这样只需要全部反转一次，然后头部的k个反转一次，剩下的再反转一次
        """
        length = len(nums)
        k %= length
        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        for i in range(start, end, 1):
            if i < end - i + start:
                nums[i], nums[end - i + start] = nums[end - i + start], nums[i]

        
# @lc code=end

