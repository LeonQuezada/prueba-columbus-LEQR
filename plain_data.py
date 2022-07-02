def plain_data(data: list):   
    result=[] 
    for item in data:        
        if type(item) is list:                                    
            result.extend(plain_data(item))
        else:
            result.append(item)
    return result