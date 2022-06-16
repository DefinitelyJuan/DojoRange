from array import array


class rango:
    def contains(firstRange:tuple, secondRange:tuple, numbers: list):
        if (firstRange[1] and secondRange[1] == False): #si es inclusivo "["
            for num in numbers:
                if (firstRange[0]<= num and secondRange[0] > num):
                    return True
                else:
                    return False
                
        if (firstRange[1] and secondRange[1] == True): 
            for num in numbers:
                if (firstRange[0]<= num and secondRange[0] >= num):
                    return True
                else:
                    return False                    
        if (firstRange[1] == False and secondRange[1] == True): 
            for num in numbers:    
                if (firstRange[0]< num and secondRange[0] >= num):
                    return True    
                else:
                    return False                                    
        if (firstRange[1] == False and secondRange[1] == False): 
            for num in numbers: 
                if (firstRange[0]< num and secondRange[0] > num):
                    return True  
                else:
                    return False                              
        else:
            return False

    def getAllPoints(firstRange:tuple, secondRange:tuple):
        numbers = []
        if (firstRange[1] and secondRange[1] == False): 
            for i in range(firstRange[0],secondRange[0]):
                numbers.append(i)
                
        if (firstRange[1] and secondRange[1] == True):
            for i in range(firstRange[0],secondRange[0]+1):
                numbers.append(i)
                
        if (firstRange[1] == False and secondRange[1] == True):
            for i in range(firstRange[0]+1,secondRange[0]+1):
                numbers.append(i) 
                                   
        if (firstRange[1] == False and secondRange[1] == False): 
            for i in range(firstRange[0]+1,secondRange[0]):
                numbers.append(i)
                            
        return numbers

    def equals(firstRange:tuple, secondRange:tuple, thirdRange:tuple, fourthRange:tuple):
        if(firstRange == thirdRange and secondRange == fourthRange):
            return True
        else:
            return False
        
    def endpoints(firstRange:tuple, secondRange:tuple): 
        endpoint = ()
        if (firstRange[1] and secondRange[1] == False): 
            endpoint = (firstRange[0], secondRange[0]-1)
                
        if (firstRange[1] and secondRange[1] == True):
            endpoint = (firstRange[0], secondRange[0])
                
        if (firstRange[1] == False and secondRange[1] == True):
            endpoint = (firstRange[0]+1, secondRange[0]) 
                                   
        if (firstRange[1] == False and secondRange[1] == False): 
            endpoint = (firstRange[0]+1, secondRange[0]-1)
        return endpoint
    def containsRange(firstRange:tuple, secondRange:tuple, thirdRange:list, fourthRange:list):
        
        if(thirdRange[1]):
            thirdRange[0] += 1
        if(fourthRange[1]):
            fourthRange[0] -= 1


        if (firstRange[1] and secondRange[1] == False): #[)
            if ((firstRange[0]<= thirdRange[0] and secondRange[0] > thirdRange[0]) and (firstRange[0]<= fourthRange[0] and secondRange[0] > fourthRange[0])):
                return True
            else:
                return False
                
        if (firstRange[1] and secondRange[1] == True): #[]
            if ((firstRange[0]<= thirdRange[0] and secondRange[0] >= thirdRange[0]) and (firstRange[0]<= fourthRange[0] and secondRange[0] >= fourthRange[0])):
                return True
            else:
                return False                    
        if (firstRange[1] == False and secondRange[1] == True):#(]
            if ((firstRange[0]< thirdRange[0] and secondRange[0] >= thirdRange[0]) and (firstRange[0]< fourthRange[0] and secondRange[0] >= fourthRange[0])):
                return True    
            else:
                return False                                    
        if (firstRange[1] == False and secondRange[1] == False):#()
            if ((firstRange[0]< thirdRange[0] and secondRange[0] > thirdRange[0]) and (firstRange[0]< fourthRange[0] and secondRange[0] > fourthRange[0])):
                return True  
            else:
                return False                              
        else:
            return False