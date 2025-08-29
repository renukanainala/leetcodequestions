class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=set()

        def check(ind,v,s1):
            if s1==0:
                ans.add(tuple(v))
            if s1<0 or ind<0:
                return
            v.append(candidates[ind])
            check(ind,v,s1-candidates[ind])
            v.pop()
            check(ind-1,v,s1)
            
        n=len(candidates)
        
        check(n-1,[],target)
        return list(ans)

            
              


        
                