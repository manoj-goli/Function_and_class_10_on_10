def top_error_ips(logs: list[str], n: int) -> list[str]:
    error_count = {}

    for log in logs:
        log = log.strip()

        log = log.split(",")

        ip = log[0] #'10.0.0.1'
        error_code = int(log[1]) #'500'

        if  500 <= error_code <= 599:
            if ip in error_count:
                error_count[ip] = error_count.get(ip,1) + 1
                #error_count= {'1':2, '2':3, '3':1, '4':2}
            else:
                error_count[ip] = error_count.get(ip,1) #{'1':1}
        error_sort = sorted(error_count.items(), key = lambda item: (item[1],item[0]), reverse=True)[:n] #   {'2':3, '1':2, '4':2, '3':1}

print(top_error_ips([
    "10.0.0.1,500",
    "10.0.0.2,200",
    "10.0.0.1,503",
    "10.0.0.3,502",
    "10.0.0.3,501"
], 2))
