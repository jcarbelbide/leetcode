from collections import deque

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        q = deque()
        q.append(0)
        longest = 1
        i = 0
        while i < len(s) and q:
            i = q.popleft()

            wild = k
            length = 0
            for j in range(i, len(s)):
                if s[j] != s[i]:
                    q.append(j)
                    wild -= 1
                    if wild < 0:
                        break
                length += 1
            longest = max(longest, length)

        i = len(s) - 1
        q.append(i)
        while i > -1 and q:
            i = q.popleft()

            wild = k
            length = 0
            for j in reversed(range(0, i+1)):
                if s[j] != s[i]:
                    q.append(j)
                    wild -= 1
                    if wild < 0:
                        break
                length += 1
            longest = max(longest, length)

        return longest


if __name__ == '__main__':
    t1 = "baaab"
    k = 2
    s = Solution.characterReplacement(0, t1, k)
    print(s)