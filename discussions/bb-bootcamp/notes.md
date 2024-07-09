# Chapter 1: Picking a Bug Bounty Program
- What is an asset? An attack surface?
- What is a social site? What are two major ways they present vulnerabilities? 
- What is triage? What are some popular BB platforms? Did you visit their sites?
- What is scope?

- Metrics for choosing a BB program
## Asset
- An application, website or product you can hack
### Social Sites and Applications
- Any site that allows users to interact with each other
- lots of potential for vulnerabilities due to complexity of interactions
- either via mismanagement of user-information or lack of validation on user input
- attack surface: application's different points that you can attempt to exploit
### General Web Applications
- No user-user interactions. Instead user-server interactions to to access app features
- Ex. static sites, cloud applications, consumer services (banking), portals of IoT
- primarily vulnerabilities on server-side + specific to application stack
### Mobile Applications
- likely need a rooted device, a regular device, and emulators for Android and iOS 
- more complex setup and likely less competitive
### APIs
- specification on how other programs interact with an organization's assets
- good APIs are key to protecting customer data
- same skillset as web-hacking
### Source Code and Executables
- once you have more experience reverse engineering
### Hardare and IoT
- even more specialized. might have to buy your own hardware
## Bug Bounty Programs
- Bounty either via BB Platforms or via independent sites
- BB examples: Bugcrowd, HackerOne, Intigriti, Synack, and Cobalt
- Search by _Company Name Bug Bounty Program_ for independent sites
- Triage: confirmation of vulnerability
### Pros 
- more transparent on amount payed, past reports, response times
- less hassle of communication with different security teams and duplicating info (tax details)
### Cons
- some companies aren't on the platform 
- chain of communication involves third party triagers who aren't as familiar with the product
## Scope, Payout and Response Times
- What and how are you allowed to attack?
- Scope involves:
    - asset scope: what subdomain, product, and application you can hack
    - vulnerability scope: what vulnerabilities companies will accept as valid bugs
- Payout Amounts: Vulnerability Disclosure Program (VDP) and Bug Bounty (BB)
- VDPs only pay is swag and reputation
## Private Programs
- Invite only. The best way to get an invite is to find something first
- sometimes possible via completing tutorials or CTFs
Tips: Choose something reputed and unpaid with big scopes and supportive team 

# Chapter 2: Sustaining your Success
Will primarily skip this chapter because it doesn't provide much technical value.
However, this will be helpful as you write reports for BB or for CTFs.
## Writing a good report
### Craft a Descriptive Title
- DONOT: IDOR on a critical endpoint
- DO: IDOR on http://example.com/change\_password Leads to Account Takeover for All Users
### Provide a clear summary
- personal pnemonic (but explained in different stages in the book):
- explain the context: what http parameters does the endpoint take?
- explain the discovery: how did you find the vulnerability?
- explain the exploit: how can the exploit be replicated?
- explain the impact: why is the exploit a concern?
### Include a Severity
- Low: Leads to potential phishing (phishing via open redirect)
- Medium: Impactful with difficult exploitation steps (CSRF on password change)
- High: Impacts a lot of users with disastrous consequences
- Critical: Impacts majority of users as well as organizational infrastructure
- Study CVSS for more: https://first.org/cvss
- Or platform-specific: https://bugcrowd.com/vulnerability-rating-taxonomy/
- https://docs.hackerone.com/hackers/severity.html
### Give Clear Steps to Reproduce
### Provide a Proof of Concept
### Describe the impact and attack Scenarios
### Recommend possible mitigation
### Validate your report
## Additional Tips
### Don't assume anything
- Is it the security team or a developer of a startup reading the report?
### Be Clear and Concise
- Do not include unnecessary details.
### Write what you want to read
### Be Professional
## Building a relationship with the Development Team
### Understanding Reporting State
- Need More Information
- Informative
- Duplicate
- N/A 
- Triaged
- Resolved
### Dealing With Conflict
### Building a Partnership
- Read some other reports with the company to understand their communication style
## Understanding Why You're Failing
### Why you are not finding bugs
- You participate in the wrong programs
- You do not stick to a program
    - Dig Deep or Search Wide
- You do not Recon 
- You go for only Low Hanging Fruit
- You do not get into private programs
### Why your report gets dismissed
- You donot read the bounty policy
- You donot put yourself in the organization's shoes
- You donot chain bugs
- You write bad reports (i.e misplaced severity)
- What about duplicates?
## What to do When you are stuck
- Take a break (rest is where creativity happens)
- Build your skill set (CTFs perhaps?)
- Gain a fresh perspective (diversify, specialize, chain)

# Chapter 3: How the Internet Works
- What is client server model?
## The client-server model
- Client requests the resources, server provides them
- HyperText Markup Language HTML decides where things are located
- Cascading Style Sheets CSS decides what they look like
- Javascript JS decides what they behave like
## Domain Name System DNS
- Computers on the internet have numbers, not names
- We assign names to these numbers using a register called DNS registry
- One computer can have many conversations at the same time. We identify a conversation
using a port number.
## HTTP Requests and Responses
- Hyper Text Transfer Protocol carries the requests and reponses
- Requests are in the format:
```http
GET / HTTP/1.1   <- Request Line
Host: www.google.com <- Header to distinguish service
Header: Value (Optional/Others)
```
- HTTP has a verb (GET, PUT, POST, DELETE, OPTIONS)
- There are a few common headers:
    - User-Agent: Browser/Curl/Python
    - Accept + Accept-Lanugage + Accept-Encoding: the format the response is expected be in
    - Connection: Should the connection stay open after sending response
    - Authorization: Credentials
    - Cookie: Some info that the server wants to save on client end
- Responses are in the format:
```http
HTTP/1.1 404 Not Found
Header: Value (Optional/Others)
Body
```
- There's a lot more at https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages
## Internet Security Controls
### Content Encoding
- Base 64 Encoding: we have covered this before on cryptopals
- URL encoding: not much except using ascii values with a preceeding % ex. %20
### Session Management and HTTP Cookies
- Why don't you have to relogin everytime?
- Server assigns a session ID then sends it to you as a cookie, which gets resent
to server with every request.
### Token-Based Authentication
- Instead of storing session ID serverside, store this into browsers itself with 
a digital signature
- JWT is a popular mechanism for it
    - { "alg": "none", "type": "JWT"} {"user": "admin"}
    - attack: manipulating the alg field
    - attack: brute-force the key
    - attack: reading sensitive information
### The Same Origin Policy
- Same Origin if same protocol, hostname and port number


# Chapter 4: Environmental Setup and Traffic Interception
- Basically install burp and configure firefox to use it
- Learn what Repeater, Decoder, Intruder, Comparer do
- Learn to save burp requests

# Chapter 5: Web Hacking Reconnaissance
- Aka gathering information
## Manually walking through the target
- Click through every page, every feature
- Sign up at each privilege level and interact
- Sign up with different account under same privilege level and interact
## Google Dorking
- practically just advanced google searches with some keywords
- site: show results from a certain site only
- inurl: show pages with url that matches search string (.php?page=)
- intitle: find search string on page's title ("index of")
- link: web pages that contain link to a specific url
- filetype: look for log files, pdf files, image files
- wildcards, minus, or (|), quotes("")
## Scope Discovery
### WHOIS and Reverse WHOIS
- whois facebook.com
- nslookup facebook.com
- whois 157.240.2.35
- track the AS for the host: whois -h whois.cymru.com 157.240.2.21
### Certificate Parsing
- Subject Alternative Name: Field has site names that use the same certificate
- with crt.sh
### Subdomain Enumeration
- sublist3r, subbrute, amass, gobuster
- You might need a list. search for SecLists
### Service Enumeration
- is a website running on any other port
- active (via your machine) or passive scanning (via a third party)
### Directory Brute Forcing
- gobuster again
### Spidering the site
- BurpSuite Crawler
- OWASP ZAP Spider
- Look at a page, go to all the pages that this page links
### Third Party Hosting
- site:s3.amazonaws.com COMPANY\_NAME
- buckets.grayhatwarefare.com for public buckets
- bruteforce using lazys3 or bucket stream
- use aws cli to interact with the buckets
### Search the organizations github repo
- Job Postings
- Way Back Machine 
- Employeers on LinkedIn, StackOverflow, Quora
- Pastebin and PasteHunter
### Tech Stack Fingerprinting
- Wapplyzer, BuiltWith, StackShare

