"""
有两个游标，都从0开始，j用来将不重复的项覆盖到前面的位置，并通过j记录不重复的长度；
i从0开始遍历，当遇到与j不相同时，将j的后面一个数赋i的值
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1