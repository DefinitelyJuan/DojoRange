class rango:
    def contains(firstRange:tuple, secondRange:tuple, numbers: list):
        if (firstRange[1] and secondRange[1] == False): #si es inclusivo "["
            for num in numbers:
                if (firstRange[0]<= num and secondRange[0] > num):
                    return True
                else:
                    return False
                
        if (firstRange[1] and secondRange[1] == True): #si es inclusivo "["
            for num in numbers:
                if (firstRange[0]<= num and secondRange[0] >= num):
                    return True
                else:
                    return False                    
        if (firstRange[1] == False and secondRange[1] == True): #si es inclusivo "["
            for num in numbers:    
                if (firstRange[0]< num and secondRange[0] >= num):
                    return True    
                else:
                    return False                                    
        if (firstRange[1] == False and secondRange[1] == False): #si es inclusivo "["
            for num in numbers: 
                if (firstRange[0]< num and secondRange[0] > num):
                    return True  
                else:
                    return False                              
        else:
            return False
