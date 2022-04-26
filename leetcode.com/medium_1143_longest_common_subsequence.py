class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        # This is a TLE
        # return rec(text1, text2, 0, 0, {})
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


def printDP(dp):
    for k in range(len(dp)):
        print(dp[k])
    print('\n')


def rec(text1, text2, i1, i2, memo):
    h = str(i1) + str(i2)
    if hash in memo:
        return memo[h]
    if i1 > len(text1) - 1 or i2 > len(text2) - 1:
        return 0

    if text1[i1] == text2[i2]:
        cell = rec(text1, text2, i1 + 1, i2 + 1, memo) + 1
        memo[h] = cell
        return cell
    # else, that means that the letters were not equal. spawn two more instances
    else:
        r1 = rec(text1, text2, i1 + 1, i2, memo)
        r2 = rec(text1, text2, i1, i2 + 1, memo)

    cell = max(r1, r2)
    memo[h] = cell

    return cell


if __name__ == '__main__':
    t1 = "pmjghexybyrgzczy"
    t2 = "hafcdqbgncrcbihkd"
    s = Solution.longestCommonSubsequence(0, t1, t2)
    print(s)
