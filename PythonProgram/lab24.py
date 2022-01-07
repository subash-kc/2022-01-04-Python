ipchk = "192.168.0.1"

# a string tests as True
if ipchk:
   print("Looks like the IP address was set: " + ipchk)


ipchk1 = input("Apply an IP address1: ") # this line now prompts the user for input

# a provided string will test true
if ipchk1:
   print("Looks like the IP address was set: " + ipchk1) # indented under if


ipchk2 = input("Apply an IP address2: ") # this line now prompts the user for input

# a provided string will test true
if ipchk2:
   print("Looks like the IP address2 was set: " + ipchk2) # indented under if
else:    # if data is NOT provided
   print("You did not provide input.") # indented under else

def main():

   ipchk3 = input("Apply an IP address3: ") # this line now prompts the user for input

# if user set IP of gateway
   if ipchk3 == "192.168.70.1":
      print("Looks like the IP address3 of the Gateway was set: " + ipchk3 + " This is not recommended.")
   elif ipchk3: # if any data is provided, this will test true
      print("Looks like the IP address3 was set: " + ipchk3) # indented under if
   else: # if data is NOT provided
      print("You did not provide input.") # indented under else

if __name__ == '__main__':
    main()

print("Subash")