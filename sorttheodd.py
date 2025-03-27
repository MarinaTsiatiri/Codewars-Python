def sort_array(source_array):
    
    odd_numbers = [num for num in source_array if num%2!=0]
    odd_numbers.sort()
    
    odd_iter = iter(odd_numbers)
    
    for i in range(len(source_array)):
        if source_array[i]%2!=0:
            source_array[i] = next(odd_iter)
            
    return source_array
