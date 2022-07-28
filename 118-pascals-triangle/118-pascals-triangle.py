class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst=[]
        for i in range(numRows+1):
            lst.append([])
        for i in range(numRows+1):
            if i==-2:
                lst[0].append(1)
            else:
                for j in range(i):
                    if j==0:
                        lst[i].append(1)
                    elif j==i-1:
                        lst[i].append(1)
                    else:
                        k=lst[i-1][j-1]+lst[i-1][j]
                        lst[i].append(k)
        return lst[1:]
                    
                
            
        