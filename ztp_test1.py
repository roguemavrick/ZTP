print "\n\n *** Sample ZTP Day0 Python Script *** \n\n"
# Importing cli module
import cli
print "\n\n *** Configuring gig 0 *** \n\n"
cli.configurep(["interface gi0", "ip address dhcp","no shut", "end"])
print "\n\n *** Configure Generic Username and password *** \n\n"
cli.configurep(["username admin password Password1", "enable password Password1"])
print "\n\n *** Configure Hostname *** \n\n"
cli.configurep(["hostname Device"])
print "\n\n *** Generate Crypto Keys *** \n\n"
cli.configurep(["crypto key gen rsa mod 1024"])
print "\n\n *** IP domain *** \n\n"
cli.configurep(["ip domain-name cisco.com"])
print "\n\n *** Set SSH version 2 *** \n\n"
cli.configurep(["ip ssh version 2"])
print "\n\n *** Set ssh transport *** \n\n"
cli.configurep(["line vty 0 15", "transport input ssh", "login local"])
print "\n\n *** Executing Save *** \n\n"
cli_command = "copy run start"
cli.executep(cli_command)
print "\n\n *** Executing show ip interface brief *** \n\n"
cli_command = "sh ip int brief"
cli.executep(cli_command)
print "\n\n *** ZTP Day0 Python Script Execution Complete *** \n\n"
