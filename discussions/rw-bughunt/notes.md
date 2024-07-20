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

# 3. HTTP Parameter Pollution (HPP)
- manipulating how a website treats parameters received during http requests
- can happen on server side or client side
## Server Side HPP
- [Paper on how servers handle parameters](https://www.owasp.org/images/b/ba/AppsecEU09_CarettoniDiPaola_v0.8.pdf)
- https://bank.com/transfer?from=myAccount&to=myAccount&amount=50000&from=yourAccount
    - how is the from processed? If latter overrides, we just took money for an arbitrary account
- the book contains a sample with array that we can pollute as well

## Client Side HPP
```html
<!-- http://host/page.php?par=123%26action=edit-->
<? $val=htmlspecialchars($_GET['par'], ENT_QUOTES); ?>
<a href="/page.php?action=view&par='.<?=$val?>'"> View Me! </a>
```

## Report 1 HackerOne Social Sharing Button
- report#: 105953
- look for links that appear to contact other services
- Visiting the page https://hackerone.com/intro?u=https://vk.com/durov
- Now on the share button, hackerone generates the link https://facebook.com/sharer.php?u=https://hackerone.com/&u=https://vk.com/durov where the latter link is used to vk.com is shared instead.
- Similarily polluting the text parameter changed the tweet that would be posted.

## Report 2 Twitter Unsubscribe Notification
- https://blog.mert.ninja/twitter-hpp-vulnerability
- unsubscribe link has ?uid=...&sig=... where sig is signature generated using uid
- Using ?uid=...&uid=...&sig=... validated signature with first uid but unsubscribed using second uid

## Report 3 Twitter Web Intent
- https://ericrafaloff.com/parameter-tampering-attack-on-twitter-web-intents/
- `follow?screen_name=...&screen_name` parameter that uses the first one to display the user info but second to actually follow

# Cross Site Request Forgery
- make a browser send request to another website
- relies on target being previously authenticated to vulnerable website
- https://bank.com?from=yourAccount&to=myAccount&amount=50000
- I get you to click on this on my website
- You are already logged in to bank.com, the request passes because of cookies
- an img tag will work just fine for CSRF on GET requests
- post forms can be autosubmitted using some javascript

- tokens can be defenses; try editing and deleting tokens
- CORS can be defences; are the correctly configured? can they be bypassed using `application/form-data` or `application/x-www-form-urlencoded` or `multipart/form-data`
- validating `Origin` or `Referer` can be defenses along with `samesite` cookies; 

- when testing, lookout for get request that modify server data

## Report 1 Shopify Twitter Disconnect
- hackerone report# 111216
- https://twitter-commerce.shopifyapps.com/auth/twitter/disconnect
- can simple get a user to disconnect using an img

## Report 2 Change Users Instacart Zome
- hackerone report# 157993
- an api endpoint `/api/v2/zones` that had no CSRF protections

## Badoo Full Account Takeover
- hackerone report# 127703
- CSRF token written in the js file. js files are not protected by CORS headers
