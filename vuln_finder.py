import subprocess
import os

os.system("clear")

print ("find your vulnerable in webite")

print ("pls wait some times to finding")

site = input("your target site:")

subprocess.call("nmap --script http-slowloris-check " + site,shell=True)
subprocess.call("nmap --script  vuln " + site,shell=True)
subprocess.call("nmap --script http-sql-injection " + site,shell=True)
subprocess.call("nmap -F " + site,shell=True)
subprocess.call("nmap --script http-exploit " + site,shell=True)
subprocess.call("nmap --script http-headers " + site,shell=True)

print ("thank you for using")
