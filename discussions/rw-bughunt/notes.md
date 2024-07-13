# 2. Open Redirect
## How Open Redirects work
- here's a toy example scenario
```bash
https://www.google.com/?redirect_to=https://www.gmail.com
```
where google.com responds with 302 to Location: www.gmail.com
However, this make the following possible:
```bash
https://www.google.com/?redirect_to=https://www.attacker.com
```
which might exploit trust and lead to phishing.

- hunting for this kind of bugs:
    - look for url parameters like redirect= or url= or r= or u=
    - look for <meta url=""> tags
    - look for window.location(.href|.replace) within javascript code

## Report 1: Shopify Theme Install Open Redirect
- hackerone report 101962
- url: https://apps.shopify.com/services/google/themes/preview/supply--blue?domain\_name=<any-domain-name>
- simply change the domain\_name parameter to whatever you like to lead the users away

## Report 2: Shopify Login Open Redirect
- hackerone report 103772
- url: http://mystore.myshopify.com/account/login?checkout\_url=.attacker.com
- ^ leads to mystore.myshopify.com.attacker.com
- browsers check the last part which takes to a malicious website

## Report 3: HackerOne Interstitial Redirect
- hackerone report 111968
- Interstitial Webpage: A page shown before redirects

Steps:
- Hacker one shows interstitial webpages "You are now leaving hackerone"
- Hacker one used zendesk for hackerone.com/zendesk\_support to handle ticketing
- Because zendesk had a open-redirect vulnerability, hackerone had the same issue
- Best to read the original report at https://web.archive.org/web/20190905135023/https://hackerone.com/reports/111968 
