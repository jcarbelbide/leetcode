class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hist = {}
        for c in s:
            if c not in hist:
                hist[c] = 1
            else:
                hist[c] += 1

        letter_count = len(s)
        for c in t:
            if c in hist:
                hist[c] -= 1
                letter_count -= 1
                if hist[c] < 0:
                    return False
            else:
                return False

        return letter_count == 0
