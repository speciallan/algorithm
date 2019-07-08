#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

class Solution:
    def moveZeroes(self, nums):
        """
        思路：将所有非0元素移到前面，再将空着的全填为0
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        count = 0
        for i in range(0, len(nums)):
            if (nums[i] != 0):
                nums[count] = nums[i]
                count += 1
        for j in range(count, len(nums)):
            nums[j] = 0

        return nums

if __name__ == '__main__':

    nums = [0,1,0,3,12]
    nums = [0,0,1]

    s = Solution()
    result = s.moveZeroes(nums)

    print(result)