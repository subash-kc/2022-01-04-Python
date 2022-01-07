#!/usr/bin/env python3
"""proto = ["ssh", "http", "https"]
print(proto)
print(proto[1])

proto.extend("dns") # this line will add d, n, and s
list.extend() iterates over whatever it was passed, where each iteration becomes a new entry at the end of the list
print(proto)"""

#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)




