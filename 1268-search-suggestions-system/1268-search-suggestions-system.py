class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        # iterate search word
        #use search word count as length to refer to the products list
        # for search word = "mo"  , length = 2
        # in products list check, if products[i][:length] == searchword:
        # output.append(products[i])
        
        # while returning sort and ans.append(output[:4])
        # output 
        
        search = ''
        ans = []
        
        for i in range(len(searchWord)):
            search += searchWord[i]   # mo
            length = len(search)     # 2
            output= []
            for j in range(len(products)):
                
                if products[j][:length] == search:
                    output.append(products[j])
            output.sort()
            ans.append(output[:3])
            # print(ans)
        return(ans)
                