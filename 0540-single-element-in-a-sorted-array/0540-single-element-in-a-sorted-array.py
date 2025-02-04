class Solution:
    def singleNonDuplicate(self, a: List[int]) -> int:
        #upto single elemet encountering element pairs found to be (even,odd)
        #aftern (odd,even)
        n=len(a)
        if n==1:
            return a[0]
        if a[0]!=a[1]:
            return a[0]
        elif a[n-1]!=a[n-2]:
            return a[n-1]
        else:
            l=1;h=n-2
            while l<=h:
                m=(h+l)//2
                if a[m]!=a[m-1] and a[m]!=a[m+1]:
                    return a[m]
                elif (( m%2==1 and a[m-1]==a[m] ) or(m%2==0 and a[m+1]==a[m])):
                    l=m+1
                else:
                    h=m-1
        
        return 1


