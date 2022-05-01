class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = deque()
        stack.append(s[0])
        lut = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for i in range(1, len(s)):
            c = s[i]
            if c not in lut:
                stack.append(c)
                continue
            elif len(stack) != 0 and stack[-1] == lut[c]:
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0


