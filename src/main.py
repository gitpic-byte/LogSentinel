import re

log_line = "Restarted server at 14:32"

pattern = r"(?P\d+)"

match = re.search(pattern, log_line)

if match:
    print("Matched text: ", match.group("status")) 
else:
    print("No match found.")

