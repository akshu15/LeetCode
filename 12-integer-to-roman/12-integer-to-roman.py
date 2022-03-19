class Solution:
    def intToRoman(self, num: int) -> str:
        hashMap={
            '1':'I',
            '5': 'V',
            '10': 'X',
            '50': 'L',
            '100': 'C',
            '500': 'D',
            '1000': 'M'
        }
        # print(hashMap['1']*3)
        
        
        def compare(str1,val,place):
            
            if val >= 1 and val < 5:  #if it lies in this range
                if place==0:
                    if val != 4:
                        str1+='I' * val
                        # print(str1)
                    else:
                        str1='IV'+str1
                
                elif place==1:
                    if val!= 4:
                        str1+='X' * val
                    else:
                        str1='XL' +str1  #40
                        
                elif place==2:
                    if val!= 4:
                        str1+='C' * val
                    else:
                        str1='CD'+str1  #400 
                        
                elif place==3:
                    if val!= 4:
                        str1+='M' * val
                    else:
                        str1='IVM'+str1  #400 
                    
                        
            elif val >= 5 and val < 10:
                
                if place==0:
                    if val!= 9:
                        str1+='V'
                        return compare(str1, val-5,place)
                    else:
                        str1='IX' +str1  #9
                        
                elif place ==1:
                    if val!= 9:
                        str1+='L' 
                        return compare(str1, val-5,place) 
                    else:
                        str1='XC'+ str1  #90
                        
                elif place ==2:
                    if val!= 9:
                        str1+='D'
                        return compare(str1, val-5,place) 
                    else:
                        str1='CM' + str1 #900
                        
                elif place ==3:
                    if val!= 9:
                        str1+='M'
                        return compare(str1, val-5,place) 
                    else:
                        str1='CM' + str1 #9000
            
            return(str1)
        
        str1=""
        str2=""
        place=0
        # num1=98
        
        num=str(num)
        
        i=len(num)-1
        while(i>=0):
            # print(num[i])
            if int(num[i])==0:
                place+=1
            
            else:
                str1+=compare(str1,int(num[i]),place)

                str2=str1 +str2
                # print(str2)
                place+=1
                str1=""
            i-=1
        return str2