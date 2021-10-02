def sum_array(array, array_size):  
    # Creating intermediate variables  
    temp_max = array[0]  
    end_max = 0  
      
    for n in range(0, array_size):  
        end_max = end_max + array[n]   
        if end_max < 0:  
            end_max = 0  
          
        elif (temp_max < end_max):  
            temp_max = end_max  
              
    return temp_max  
# input array    
array = [3, -5, 4, -1, -2, 6, -8]  
print("Maximum value in the array:", sum_array(array, len(array))) 