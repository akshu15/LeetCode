class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits)==0:
            return
        
        else:
        
            hashMap={
                '2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
            }

            
            letter_list=[]

            for d in digits:
                letter_list.append(hashMap[d])

            # print(letter_list)
            
            if len(digits)==1:
                return hashMap[digits]
            
            

            while len(letter_list)>1:
                list1 = letter_list.pop()
                list2 = letter_list.pop()

                combo=[]

                for ch1 in list1:
                    for ch2 in list2:

                        combo.append(ch2 + ch1)

                letter_list.append(combo)

            return letter_list[0]
            
            
            
        # return [] if not letter_list else letter_list[0]
            # print(i,j)
        