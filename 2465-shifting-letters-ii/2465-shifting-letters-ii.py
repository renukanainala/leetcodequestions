class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        s1 = [0] * (n + 1)
        for start, end, d in shifts:
            s1[start] += 1 if d == 1 else -1
            if end + 1 < n:
                s1[end + 1] -= 1 if d == 1 else -1
        c = 0
        r = []
        for i in range(n):
            c += s1[i]
            net = (c % 26 + 26) % 26
            char = chr((ord(s[i]) - ord('a') + net) % 26 + ord('a'))
            r.append(char)

        return ''.join(r)
