#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 1:
            return s

        # if len(s) == 2 and s[0] == s[1]:
        #     return s

        # f1 aba
        arr1 = []
        for i in range(0, len(s)-1):
            center, width = self.f1(s, i, 0)
            # print('f1:', i, center, width)

            ss = s[center-width:center+width+1]
            # print(ss)
            arr1.append(ss)

        # f2 abba
        for i in range(0, len(s)-1):
            center, width = self.f2(s, i, 0)
            # print('f2:', i, center, width)

            ss = s[center-width+1:center+1+width]
            # print(ss)
            arr1.append(ss)

        max = 0
        max_str = ''
        for i in range(len(arr1)):
            if len(arr1[i]) > max:
                max = len(arr1[i])
                max_str = arr1[i]

        return max_str


    def f1(self, s, center, width):

        # 超边界为空 结束条件
        if center-width-1 < 0 or center+width+1 > len(s)-1:
            return center, width

        # 一种情况 aba
        if s[center-width-1] == s[center+width+1]:
            return self.f1(s, center, width+1)
        else:
            # 找到不同的终止
            return center, width


    def f2(self, s, center, width):

        # 超边界为空 结束条件
        if center-width < 0 or center+width+1 > len(s)-1:
            return center, width

        # 一种情况 abba
        # print(center, width)
        if s[center-width] == s[center+1+width]:
            return self.f2(s, center, width+1)
        else:
            # 找到不同的终止
            return center, width



if __name__ == "__main__":

    # s = "ababad"
    # s = "abcdccda"
    # s = "bb"
    s = 'cbbb'
    # s = 'ac'
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    solution = Solution()
    result = solution.longestPalindrome(s)
    print(result)
