class Solution:
    def countCompleteSubarrays(self, s: List[int]) -> int:
        k=len(set(s))
        r=0
        l=0
        n=len(s)
        h={}
        c=0
        while r<n:
            while l<n and len(h)<k:
                if s[l] in h:
                    h[s[l]]+=1
                else:
                    h[s[l]]=1
                l+=1
            if l==n and len(h)<k:
                break
            c+=n-l+1
            h[s[r]]-=1
            if h[s[r]]==0:
                del h[s[r]]
            r+=1
        return c