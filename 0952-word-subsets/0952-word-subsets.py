class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        f4=[0]*26
        #f=[0]*26
        for i in words2:
            f=[0]*26
            for j in i:
                f[ord(j)-97]+=1#frequency array of words2
            for k in range(26):
                f4[k]=max(f4[k],f[k])
        ans=[]
        for i in words1:
            f1=[0]*26# for each word
            for j in i:
                f1[ord(j)-97]+=1 #frequency of each letter
            f3=False
            for j in range(26):
                if  f4[j]!=0 and f1[j]<f4[j]:
                   f3=True
                   break
           # print(f3)
            if not f3:
                ans.append(i)
        return ans

        