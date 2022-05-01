class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = s[0]
        N = len(s)

        for i in range(N):
            for offset in range(1, 3):
                left = i
                right = left + offset
                while left >= 0 and right < N and s[left] == s[right]:
                    pal = s[left:right + 1]
                    longest = pal if len(pal) > len(longest) else longest
                    left -= 1
                    right += 1

        return longest