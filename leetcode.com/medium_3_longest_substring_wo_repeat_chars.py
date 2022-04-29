class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        i, j = 0, 1
        longest = 0
        hist = {s[0]: 0}
        while j < len(s):
            print(s[i:j+1], hist, i, j)
            if s[j] in hist:
                i = max(i, hist[s[j]] + 1)

            longest = max(longest, j - i + 1)
            hist[s[j]] = j
            j += 1

        return longest


if __name__ == '__main__':
    s = Solution.lengthOfLongestSubstring(1, "tmmzuxt")
    print(s)
