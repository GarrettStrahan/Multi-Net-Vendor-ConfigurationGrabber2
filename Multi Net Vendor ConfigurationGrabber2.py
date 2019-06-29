#Configured with Windows10, modify if your Linux
#Python 3.7
#This will grab your configuration + Interface information from either Juniper, Cisco

from netmiko import Netmiko
import sys  #this is only for the feature HP_ProCurve it will make the program quit. When this is fully supported I will get rid of this line of code more than likely


def writetohdd(interfaces, shrun):
    File_object = open("Interfaces.txt", "w")
    File_object.write(interfaces)
    print("The interfaces has been been written to Interfaces.txt")

    File_object2 = open("Running-Config.txt", "w")
    File_object2.write(shrun)
    print("The Running-configuration has been been written to Running-Config.txt")

def junipercon(ipaddr, username, password, networknodetype):

    from netmiko import ConnectHandler

    juniperconnect = {
        "host": ipaddr,
        "username": username,
        "password": password,
        "device_type": networknodetype}
#   net_connect = Netmiko(**juniperconnect)  # This is where it connect with SSH for no enable/secret
    net_connect = ConnectHandler(**juniperconnect, global_delay_factor=2)

    shrun = net_connect.send_command('show configuration')
    print(net_connect.send_command('show configuration'))
    print("\n")
    interfaces = net_connect.send_command("show interfaces terse")
    print(net_connect.send_command("sh run"))
    net_connect.disconnect()
    writetohdd(interfaces, shrun)



def cisco_con(ipaddr, username, password, secret, networknodetype):

    if secret == "none":
        ciscoconnectnoenable = {
            "host": ipaddr,
            "username": username,
            "password": password,
            "device_type": networknodetype}
        net_connect = Netmiko(**ciscoconnectnoenable)  # This is where it connect with SSH for no enable/secret

    elif secret != "none":
        ciscoconnectwithenable = {
            "host": ipaddr,
            "username": username,
            "secret": secret,
            "password": password,
            "device_type": networknodetype}
        net_connect = Netmiko(**ciscoconnectwithenable)  # This is where it connect with SSH

    print("\n")
    print(net_connect.find_prompt())
    print(net_connect.enable())
    print(net_connect.send_command("sh clock"))
    clock = net_connect.send_command("sh clock")
    print(net_connect.send_command("sh int ip brief"))
    interfaces = net_connect.send_command("sh int ip brief")
    shrun = net_connect.send_command("sh run")
    print(net_connect.send_command("sh run"))

    net_connect.disconnect()
    WriteToHDD(interfaces, shrun)

def ciscoasacon(ipaddr, username, password, secret, networknodetype):
    if secret == "none":
        CiscoASAConnectNoEnable = {
            "host": ipaddr,
            "username": username,
            "password": password,
            "device_type": networknodetype}
        net_connect = Netmiko(**CiscoASAConnectNoEnable)  # This is where it connect with SSH for no enable/secret

    elif secret != "none":
        CiscoASAConnectWithEnable = {
            "host": ipaddr,
            "username": username,
            "secret": secret,
            "password": password,
            "device_type": networknodetype}
        net_connect = Netmiko(**CiscoASAConnectWithEnable)  # This is where it connect with SSH

    print("\n")

    print(net_connect.find_prompt())
    print(net_connect.enable())
    print(net_connect.send_command("sh clock"))
    clock = net_connect.send_command("sh clock")
    print(net_connect.send_command("sh int ip brief"))
    interfaces = net_connect.send_command("sh int ip brief")
    shrun = net_connect.send_command("sh run")
    print(net_connect.send_command("sh run"))

    net_connect.disconnect()
    writetohdd(interfaces, shrun)



ipaddr = input("What is the IP-Address?")
username = input("What is the username?")
password = input("What is the password?")
secret = input("What is the enable password? if none state none")

if secret =="NONE":
    secret.lower

networknodetype = input("What type of device are you trying to connect to:? \n 1.Regular Cisco Device. \n  2.Cisco ASA. \n  3.Juniper. \n 4.Juniper SRX \n  5.HP ProCurve")

if networknodetype == "1": #Regular Cisco
    networknodetype = 'cisco_ios'
    cisco_con(ipaddr, username, password, secret, networknodetype)

if networknodetype == "2": #Cisco ASA
    networknodetype = 'cisco_asa'
    ciscoasacon(ipaddr, username, password, secret, networknodetype)

if networknodetype == "3": #Juniper
     networknodetype = 'juniper_junos'
     junipercon(ipaddr, username, password, networknodetype)

if networknodetype == "4": #Juniper-SRX
    networknodetype = 'juniper'
    junipercon(ipaddr, username, password, networknodetype)

if networknodetype == "5": #HP ProCurve
    networknodetype = 'hp_procurve'
    print("Please close the program this is not fully supported as of yet")
    sys.exit(0)















# 5

# print()
# print(net_connect.find_prompt())
# print(net_connect.enable())
# print(net_connect.send_command("sh clock"))
# clock =  net_connect.send_command("sh clock")
# print(net_connect.send_command("sh int ip brief"))
# interfaces = net_connect.send_command("sh int ip brief")
# shrun = net_connect.send_command("sh run")
# print(net_connect.send_command("sh run"))
#
# net_connect.disconnect()
#
# print("WE HAVE DISCONNECTED")
# print(clock)
# print(interfaces)
# print(type(interfaces))


