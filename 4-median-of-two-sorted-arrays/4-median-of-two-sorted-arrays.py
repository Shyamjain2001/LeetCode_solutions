class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merj(a,b):
            lst=[]
            len_a,len_b=len(a),len(b)
            i=j=0
            while len_a>i and len_b>j:
                if a[i]>b[j]:
                    lst.append(b[j])
                    j+=1
                else:
                    lst.append(a[i])
                    i+=1
            while len_a>i:
                lst.append(a[i])
                i+=1
            while len_b>j:
                lst.append(b[j])
                j+=1
            return lst 
        k=merj(nums1,nums2)
        a,b=len(nums1),len(nums2)
        mid=len(k)//2
        if len(k)%2==0:
            return (k[mid]+k[mid-1])/2
        else:
            return k[mid]
        
                    
        