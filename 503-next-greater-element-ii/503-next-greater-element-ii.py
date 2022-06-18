class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        lst=nums+nums
        print(lst)
        vect=[]
        sect=[]
        n=len(lst)
        for i in range(n-1,-1,-1):
            if sect==[]:
                vect.append(-1)
                sect.append(lst[i])
            elif sect[-1]>lst[i]:
                vect.append(sect[-1])
                sect.append(lst[i])
            else:
                while len(sect)>=0:
                    if len(sect)==0:
                        vect.append(-1)
                        sect.append(lst[i])
                        break 
                    k=sect.pop()
                    if k>lst[i]:
                        vect.append(k)
                        sect.append(k)
                        sect.append(lst[i])
                        break 
        vect=vect[::-1]
        return vect[:len(nums)]
        