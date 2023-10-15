import subprocess
import optparse
import random
import re

def user_input():
    obj = optparse.OptionParser()
    obj.add_option("-i","--interface",dest="interface",help="---")
    return obj.parse_args()

def fastmac():
    mac = "00:XX:XX:XX:XX:XX"
    mac = re.sub('X', lambda x: random.choice('0123456789ABCDEF'), mac)
    return mac


def change(mac,interface):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])

def control(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(f"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("----------------old-------------")

(user_input, arguments) = user_input()
interface = user_input.interface
mac = fastmac()
old_mac = control(interface)
print(f"Old MAC address: {old_mac}")

print("----------------new-------------")
change(mac, interface)
new_mac = control(interface)
print(f"New MAC address: {new_mac}")