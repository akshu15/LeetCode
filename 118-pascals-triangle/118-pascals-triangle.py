class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        final=[[1]]
        
        for k in range(numRows-1):
            
            # print(final)
            # l.insert(0,0)
            # l.append(0)
            
            l=[0]+final[-1]+[0]
            print(l)
            temp=[]
            
            i=0
            j=1
            while i<len(l)-1 and j<len(l):

                temp.append(l[i]+l[j])
                
                i+=1
                j+=1
        
            final.append(temp)
        return(final)
            # l=temp

            
            
            