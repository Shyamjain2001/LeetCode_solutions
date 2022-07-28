class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n=rowIndex
        if n==0:
            return [1]
        elif n==1:
            return [1,1]
        else:
            lst=[]
            for i in range(n+1):
                if i==0:
                    lst.append(1)
                elif i==n:
                    lst.append(1)
                else:
                    k=lst[i-1]*(n-i+1)
                    k=int(k/(i))
                    lst.append(k)
        return lst