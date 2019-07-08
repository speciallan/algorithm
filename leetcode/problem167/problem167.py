#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        length = len(numbers)

        min = 0
        max = length - 1

        flag = 'left'
        print(min, max)

        while (min < max):

            if numbers[min] + numbers[max] == target:
                return [min+1, max+1]
            elif numbers[min] + numbers[max] < target:
                min += 1
            else:
                max -= 1

            # if flag == 'left':
            #     min += 1
            #     flag = 'right'
            #
            #     while (min < length -1 and numbers[min] == numbers[min+1]):
            #         min += 1
            #
            # print(min, max)
            # if numbers[min] + numbers[max] == target and min != max:
            #     return [min+1, max+1]
            #
            # if flag == 'right':
            #     max -= 1
            #     flag = 'left'
            #     while (max > 0 and numbers[max] == numbers[max-1]):
            #         max -= 1
            #
            # print(min, max)
            # if numbers[min] + numbers[max] == target and min != max:
            #     return [min+1, max+1]



if __name__ == '__main__':

    numbers = [2, 7, 11, 15]
    target = 9

    s = Solution()
    result = s.twoSum(numbers, target)

    print(result)



