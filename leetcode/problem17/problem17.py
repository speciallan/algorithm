#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return []

        letter = digits[len(digits)-1]
        str = digits[0:len(digits)-1]

        # print(str, '-', letter)
        # exit()

        return self.f(str, letter)


    def f(self, str, letter):

        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}

        # 单个数字
        if len(str) == 0 and len(letter) == 1:
            return dic[letter]

        # '1' '2'得到所有组合
        if len(str) == 1 and len(letter) == 1:
            s = []
            for i in range(len(dic[str])):
                for j in range(len(dic[letter])):
                    s.append(dic[str][i] + dic[letter][j])
            return s

        else:
            last_letter = letter
            letter = str[len(str)-1]
            str = str[0:len(str)-1]

            arr = self.f(str, letter)
            new_arr = []

            for i in range(len(arr)):
                for j in range(len(dic[last_letter])):
                    new_arr.append(arr[i] + dic[last_letter][j])

            return new_arr

if __name__ == "__main__":

    digits = "234"
    # digits = ""

    solution = Solution()
    result = solution.letterCombinations(digits)
    print(result)