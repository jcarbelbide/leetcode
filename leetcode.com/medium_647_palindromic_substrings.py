class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = len(s)
        N = len(s)

        for i in range(N):
            for offset in range(1, 3):
                left = i
                right = left + offset
                while left >= 0 and right < N and s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1

        return res

