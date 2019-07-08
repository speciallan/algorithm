#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

class Solution:
    def plusOne(self, digits):

        # 1 2 9
        # input = input().split()
        # arr = []
        #
        # arr.append(0)
        # for k,v in enumerate(input):
        #     arr.append(int(v))

        arr = []

        arr.append(0)
        for k,v in enumerate(digits):
            arr.append(v)

        length = len(arr)

        max = length - 1
        min = 0

        cur = max
        sum = arr[cur] + 1

        while (cur >= min):

            if sum == 10:
                arr[cur] = 0
                cur -= 1
                sum = arr[cur] + 1
            else:
                arr[cur] = sum
                break

        if length > 1 and arr[0] == 0:
            arr.remove(0)

        return arr


if __name__ == '__main__':

    digits = [1, 2, 9]
    # digits = [0]

    s = Solution()
    result = s.plusOne(digits)

    print(result)
