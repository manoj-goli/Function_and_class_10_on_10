def top_error_ips(logs: list[str], n: int) -> list[str]:
    
    error_count = {}
    
    for log in logs:
        log = log.strip()
        if not log or log.startswith("#"):
            continue
        log = log.split(",")
        if len(log) != 2:
            raise ValueError("Invalid inputs")
        
        ip = log[0] #'10.0.0.1'
        
        try:
            
            error_code = int(log[1]) #'500'
        except:
            continue
        
        
        if  500 <= error_code <= 599:
            if ip in error_count:
                error_count[ip] = error_count.get(ip,1) + 1 
                #error_count= {'1':2, '2':3, '3':1, '4':2}
            else:
                error_count[ip] = error_count.get(ip,1) #{'1':1}
        else:
            continue
        try:
            n = int(n)
        except:
            raise ValueError("Invalid n value")
        if n > 0:
            error_sort = sorted(error_count.items(), key = lambda item: (item[1],item[0]))[:n] #   {'2':3, '1':2, '4':2, '3':1}
        else:
            error_sort = []
        
    # final_output = [item[0] for item in error_sort]
    # return final_output
    updatedlist = []
    for item in error_sort:
        updatedlist.append(item[0])
    return updatedlist
        
        
print(top_error_ips(["10.0.0.1,500","10.0.0.1,503","10.0.0.3,502","10.0.0.3,501", "10.0.0.3,abc"], 2))

#Big O Notation:
# The time complexity of the top_error_ips function is O(m log m) where m is the number of unique IP addresses with error codes in the logs. This is because we need to sort the error_count dictionary items based on their counts and IP addresses.
# The space complexity of the top_error_ips function is O(m) where m is the number of unique IP addresses with error codes in the logs. This is because we need to store the error counts for each unique IP address in the error_count dictionary.
# Additionally, the space complexity of the final output list is O(n) where n is the number of top IP addresses requested. However, since n is typically much smaller than m, we can consider the overall space complexity to be O(m).
# In summary, the top_error_ips function has a time complexity of O(m log m) and a space complexity of O(m).