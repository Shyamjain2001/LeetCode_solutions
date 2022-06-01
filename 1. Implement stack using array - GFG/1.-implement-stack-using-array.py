#User function Template for python3

class MyStack:
   
   def __init__(self):
       self.arr=[]
   
   #Function to push an integer into the stack.
   def push(self,data):
       #add code here
       self.arr.append(data)
   
   #Function to remove an item from top of the stack.
   def pop(self):
       #add code here
      
       
       
       if len(self.arr)==0:
           return -1
           
       
       else:
           e=self.arr[len(self.arr)-1]
           del self.arr[len(self.arr)-1]
           return e
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyStack()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
# } Driver Code Ends