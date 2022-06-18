class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=nums2
        vect=[]
        stk=[]
        n=len(lst)
        for i in range(n-1,-1,-1):
            #print(stk)
            if stk==[]:
                vect.append(-1)
                stk.append(lst[i])
            elif stk[-1]>=lst[i]:
                vect.append(stk[-1])
                stk.append(lst[i])
            else:
                while len(stk)>=0:
                    if len(stk)==0:
                        vect.append(-1)
                        stk.append(lst[i])
                        break
                    t=stk.pop()
                    if t>=lst[i]:
                        vect.append(t)
                        stk.append(t)
                        stk.append(lst[i])
                        break
        vect=vect[::-1]
        dt={}
        for i in range(n):
            dt[lst[i]]=vect[i]
        op=[]
        for i in nums1:
            op.append(dt[i])
        return op