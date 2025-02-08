class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        if S == ' ': return True
        if S > T: return False

        j = 0
        for i in range(T):
            if j < S and t[i] == s[j]: 
                j += 1
                if j == S:
                    return True
        return j == S
