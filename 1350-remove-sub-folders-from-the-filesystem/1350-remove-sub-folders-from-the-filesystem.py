class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res=[]
        
        for i in folder:
            if not res:
                res.append(i)
                
            else:
                prev=res[-1]
                if prev==i[:len(prev)] and i[len(prev)]=='/':
                    continue
                else:
                    res.append(i)
        return res
                

        