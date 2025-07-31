import requests 
import sys 

# SPECIFY THE NAME OF WORDLIST FILE BELOW
sub_list = open("subdomains.txt").read() 
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"https://{sub}.{sys.argv[1]}" 

    try:
        requests.get(sub_domains)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domains)   
