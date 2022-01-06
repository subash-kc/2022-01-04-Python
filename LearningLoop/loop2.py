# create a list of strings
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]

# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]

for x in vendors:
    print("n\The vendor is " + x, end="")
    if x not in approved_vendors:
        print("- NOT AN APPORVED VENDOR!", end="")