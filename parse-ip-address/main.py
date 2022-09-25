import socket
# get hostname and ip address of a computer or remote server
host_name = socket.gethostname()
print ("hostname is:", host_name)
IP_address = socket.gethostbyname(host_name)
print("Computer IP Address is", IP_address)

# get IP Address from hostname
host_name = input("Enter the website address: ")
print(f'The {host_name} IP address is: {socket.gethostbyname(host_name)}')


# check if an ip_address is public or private

from ipaddress import ip_address

def IP_address(IP: str)-> str:
    return "Private" if (ip_address(IP).is_private)else "Public"

if __name__ == '__main__':
    print(IP_address('142.250.203.142'))
    print(IP_address('127.0.0.1'))
    
#check the validity of an ip address
IP = '127.0.0.1'
try:
   socket.inet_aton(IP)
   print("Valid IP address")
except socket.error:
   print("Invalid IP")
   
# get the mac address of your computer
import re, uuid
print("MAC address is:", end="")
print(':'.join(re.findall('..', '%012x' %uuid.getnode())))
