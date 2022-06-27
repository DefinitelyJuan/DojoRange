
class rango:
    def __init__(self, strRange:str):
        try:
            self.lNumber = strRange[1:strRange.find(",")]
            self.lInclusive = True if strRange[0] == "[" else False
            self.rNumber = strRange[strRange.find(",")+1:-1]
            self.rInclusive= True if strRange[-1] == "[" else False

        except:
            raise Exception("Invalid String. May have invalid format, should be like this: [1,5)")
        assert self.lNumber <= self.rNumber, "right number should be greater than left"
    def contains(self, numbers: list):
        if (self.lInclusive and self.rInclusive == False): #si es inclusivo "["
            for num in numbers:
                if (self.lNumber<= num and self.rNumber > num):
                    return True
                else:
                    return False
                
        if (self.lInclusive and self.rInclusive == True): 
            for num in numbers:
                if (self.lNumber<= num and self.rNumber >= num):
                    return True
                else:
                    return False                    
        if (self.lInclusive == False and self.rInclusive == True): 
            for num in numbers:    
                if (self.lNumber< num and self.rNumber >= num):
                    return True    
                else:
                    return False                                    
        if (self.lInclusive == False and self.rInclusive == False): 
            for num in numbers: 
                if (self.lNumber< num and self.rNumber > num):
                    return True  
                else:
                    return False                              
        else:
            return False

    def getAllPoints(self):
        numbers = []
        if (self.lInclusive and self.rInclusive == False): 
            for i in range(self.lNumber,self.rNumber):
                numbers.append(i)
                
        if (self.lInclusive and self.rInclusive == True):
            for i in range(self.lNumber,self.rNumber+1):
                numbers.append(i)
                
        if (self.lInclusive == False and self.rInclusive == True):
            for i in range(self.lNumber+1,self.rNumber+1):
                numbers.append(i) 
                                   
        if (self.lInclusive == False and self.rInclusive == False): 
            for i in range(self.lNumber+1,self.rNumber):
                numbers.append(i)
                            
        return numbers

    def equals(firstRange:tuple, secondRange:tuple, thirdRange:tuple, fourthRange:tuple):
        if(firstRange == thirdRange and secondRange == fourthRange):
            return True
        else:
            return False
        
    def endpoints(self): 
        endpoint = ()
        if (self.lInclusive and self.rInclusive == False): 
            endpoint = (self.lNumber, self.rNumber-1)
                
        if (self.lInclusive and self.rInclusive == True):
            endpoint = (self.lNumber, self.rNumber)
                
        if (self.lInclusive == False and self.rInclusive == True):
            endpoint = (self.lNumber+1, self.rNumber) 
                                   
        if (self.lInclusive == False and self.rInclusive == False): 
            endpoint = (self.lNumber+1, self.rNumber-1)
        return endpoint
    def containsRange(firstRange:tuple, secondRange:tuple, thirdRange:list, fourthRange:list):
        

        if(not thirdRange[1]):
            thirdRange[0] += 1
        if(not fourthRange[1]):
            fourthRange[0] -= 1



        if (self.lInclusive and self.rInclusive == False): #[)
            if ((self.lNumber<= thirdRange[0] and self.rNumber > thirdRange[0]) and (self.lNumber<= fourthRange[0] and self.rNumber > fourthRange[0])):
                return True
            else:
                return False
                
        if (self.lInclusive and self.rInclusive == True): #[]
            if ((self.lNumber<= thirdRange[0] and self.rNumber >= thirdRange[0]) and (self.lNumber<= fourthRange[0] and self.rNumber >= fourthRange[0])):
                return True
            else:
                return False                    
        if (self.lInclusive == False and self.rInclusive == True):#(]
            if ((self.lNumber< thirdRange[0] and self.rNumber >= thirdRange[0]) and (self.lNumber< fourthRange[0] and self.rNumber >= fourthRange[0])):
                return True    
            else:
                return False                                    
        if (self.lInclusive == False and self.rInclusive == False):#()
            if ((self.lNumber< thirdRange[0] and self.rNumber > thirdRange[0]) and (self.lNumber< fourthRange[0] and self.rNumber > fourthRange[0])):
                return True  
            else:
                return False                              
        else:
            return False
    
    def overlapsRange(firstRange:list, secondRange:list, thirdRange: list, fourthRange:list): 
        
        if(not thirdRange[1]):
            thirdRange[0] += 1
        if(not fourthRange[1]):
            fourthRange[0] -= 1
        
        if(not self.lInclusive):
            thirdRange[0] += 1
        if(not self.rInclusive):
            fourthRange[0] -= 1
     
        #2,8-1
        overlapset = set(range(self.lNumber, self.rNumber+1))
        if (len(overlapset.intersection(range(thirdRange[0], fourthRange[0]+1)))>0):
            return True 
        else:
            return False



