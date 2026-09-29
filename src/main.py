import re

log_list = "Found breach attempts at port 450 switching to port 230"

pattern = r"port (?P<first_port>\d+) .*? port (?P<second_port>\d+)"

match = re.search(pattern, log_list)

print(match.group("first_port"))   # 450
print(match.group("second_port"))  # 230

