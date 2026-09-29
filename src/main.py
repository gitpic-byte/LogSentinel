import re

log_line = "Client 192.168.1.1 returned status 404"

# 1. We define custom names inside < >: "IP" and "status"
pattern = r"Client (?P\S+) returned status (?P\d+)"

match = re.search(pattern, log_line)

if match:
    # Accessing individually by name:
    print("IP Address:", match.group("IP"))
    print("Status Code:", match.group("status"))
    
    print("---")
    
    # Converting ALL named groups into a dictionary:
    log_data = match.groupdict()
    print("Dictionary output:", log_data)