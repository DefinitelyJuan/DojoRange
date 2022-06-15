class rango:
    def contains(firstRange:tuple, secondRange:tuple, number1:int,number2:int):
        if (firstRange[1] and secondRange[1] == False): #si es inclusivo "["
                if (firstRange[0]<= number1 and secondRange[0] > number2):
                    return True
                else:
                    return False
                
        if (firstRange[1] and secondRange[1] == True): #si es inclusivo "["
                if (firstRange[0]<= number1 and secondRange[0] >= number2):
                    return True
                else:
                    return False                    
        if (firstRange[1] == False and secondRange[1] == True): #si es inclusivo "["
                if (firstRange[0]< number1 and secondRange[0] >= number2):
                    return True    
                else:
                    return False                                    
        if (firstRange[1] == False and secondRange[1] == False): #si es inclusivo "["
                if (firstRange[0]< number1 and secondRange[0] > number2):
                    return True  
                else:
                    return False                              
        else:
            return False
