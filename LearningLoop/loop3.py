# for-loop is perfect for stepping through this list
iplist = ["10.1.1.1", "10.2.2.2", "10.3.3.3"] # list of IP (str)

# 'ip' is just a variable as we step through iplist
for ip in iplist:
    print(ip)   # we indent to show this is the code we want to run each time
                # through the loop

dnsfile = open("dnsservers.txt", "r")

dnslist = dnsfile.readlines()

print()
for svr in dnslist:
    print(svr, end="")