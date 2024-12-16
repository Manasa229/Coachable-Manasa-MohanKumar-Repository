"""5. Longest Palindromic Substring"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        """
        - Take the substrings of the string
        -check if the substring is palidrome
        -if true, check if the length is greater than the res length, if true updatre res
        - return res

        Time Complexity:O(n^2)
        Space Complexity:O(n)
        """

        res = ""

        def _isPalindrome(i, j):
            nonlocal res
            substring = ""
            while i >= 0 and j < len(s):

                if s[i] != s[j]:
                    break
                substring = s[i:j + 1]
                i -= 1
                j += 1

            if len(substring) > len(res):
                res = substring

        for i in range(len(s)):
            _isPalindrome(i, i)
            _isPalindrome(i, i + 1)

        return res