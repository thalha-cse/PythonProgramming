# This project is defang IP address
# To convert an IP address to a defanged IP address, we need to replace "." with "[.]"

def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
ipaddress = ip_address("1.1.2.3")
print(ipaddress)
