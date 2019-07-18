#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        if n == 1:
            return True

        # yushu = n % 10
        #
        # if yushu not in [2, 4, 6, 8]:
        #     return False

        bi_num = bin(n)[2:]

        if bi_num[0] == '1':
            i = 1
            while i <= len(bi_num) - 1:
                if bi_num[i] == '0':
                    i += 1
                else:
                    return False

        return True

if __name__ == "__main__":

    n = 4

    solution = Solution()
    result = solution.isPowerOfTwo(n)
    print(result)
