class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n=len(words)
        ans=[]
        for i in range(n):
            for j in range(n):
                if words[j]==words[i]:
                    continue
                else:
                    if words[i] in words[j]:
                        ans.append(words[i])
                        break
        print(ans)
        return ans

