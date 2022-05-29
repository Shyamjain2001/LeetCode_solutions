class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=[],[]
        lm=-1
        rm=-1
        for i in height:
            if i>lm:
                left.append(i)
                lm=i 
            else:
                left.append(lm)
        #print(left)
        riv=[]
        for i in height:
            riv.insert(0,i)
        #print(riv)
        for i in riv:
            if i>rm:
                right.append(i)
                rm=i 
            else:
                right.append(rm)
        #print(right)
        rr=[]
        for i in right:
            rr.insert(0,i)
        #print(height)
        area=0
        for i in range(len(height)):
            area+=min(left[i],rr[i])-height[i]
        return area
            
            
        