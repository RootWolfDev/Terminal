import requests
import socket
import shutil
import marshal
import argparse
from rich import print
from rich.console import Console


#the theme
def textascii():
    print(r"""[red]
                            
                      __   
 ___.__. ____   _____/  |_ 
<   |  |/    \_/ __ \   __\
 \___  |   |  \  ___/|  |  
 / ____|___|  /\___  >__|  
 \/         \/     \/      
""")
demand=None

def start():
     global demand
     console = Console()
     demand = console.input("([red]yabby_net[/])> ").split()
     return demand
     

#this is the documentation of this tool
def help():
    print('__DNS cheking__')
    print('always start with ynet')
    documentation={'chek ip':'-Ip',
          'chek webscarping ':'-Pg',
          'technology enumeration':'-Te',
          'whois':'-Ws',
          'get a file':'-Gt',
          'chek port':'-P'}
    for key, value in documentation.items():
        print(f'[red]{key}[/]:[green]{value}[/]')

def line():
    terminal_width = shutil.get_terminal_size().columns
    print("-" * terminal_width)
def Tool():
    def parse_commands(input_args):
        parser = argparse.ArgumentParser(description="ynet")
        parser.add_argument('ynet')
        parser.add_argument('-P', action='store_true')
        parser.add_argument('-Ip', action='store_true')
        parser.add_argument('-Pg',  action='store_true')
        parser.add_argument('-Te', action='store_true')
        parser.add_argument('-Gt', action='store_true')
        parser.add_argument('-Ws', action='store_true')
        parser.add_argument('exit', action='store_true')

        


        args, remaining = parser.parse_known_args(input_args)

        domainy = remaining[0] if remaining else "None"

        return args, domainy
    global demand
    options, target = parse_commands(demand)
    result=demand
    domain=target
    used= False

    if 'ynet' in result:
        used=True
        #('chek ip':'-Ip'):
    if '-Ip' in result :
        line()
        try:
            ip= socket.gethostbyname(domain)
            print(f'ip adress:{ip}')
        except: 
            try: 
                print('[red]error to know the ip')
            except: 
                pass      
        used=True
        #('whois':'-Ws')
    if '-Ws' in result:
        line()
        whois=requests.get(f'https://api.whois.vu/?q={domain}')
        print('Whois\n',whois.text)
        used=True
        #('technology enumeration':'-Te')
    if '-Te' in result:
        line()
        try:
            response = requests.get(f'http://{domain}')
        except:
            try:
                response = requests.get(f'https://{domain}')
            except:
                urld = input('give me the url: ')
                response = requests.get(urld)
        for x,y in response.headers.items():
            print(f'{x}:{y}')
            #('chek webscarping ':'-Pg')
    if '-Pg' in result:
        line()
        urls = [
            f'https://{domain}/',
            f'https://www.{domain}/',
            f'http://{domain}/',
            f'http://www.{domain}/',
        ]

        ping_success = False

        for url in urls:
            try:
                ping = requests.get(url, timeout=5)
                status = ping.status_code

                if 200 <= status < 400:
                    print(f'[green]Ping OK:[/] {url} (Status: {status})')
                    ping_success = True
                    break  # if one is OK, no need to try others
                else:
                    print(f'[yellow]Site reachable but error status:[/] {url} (Status: {status})')

            except requests.RequestException as e:
                print(f'[red]Failed to reach:[/] {url} ({e})')

        if not ping_success:
            try:
                custom = input('All attempts failed. Give me the full URL: ')
                ping = requests.get(custom, timeout=5)
                print(f'[green]Ping OK:[/] {custom} (Status: {ping.status_code})')
            except Exception:
                print('[red]Error!![/]')
    if '-Gt' in result :
        line()
        try:
            file_url=input('url_file:')
            name_file=input('name of file:')
            file_get=requests.get(file_url)
            with open(name_file,"wb") as f:
                f.write(file_get.content)
        except:
            print('[red]error![/]')
            #good!!
    if '-P' in result :
        line()

        ping_success = False
        port=0	


    protocols = ["https://", "http://"]
    base_url = None

    for proto in protocols:
        try:
            test_url = proto + domain
            r = requests.get(test_url, timeout=5)
            if r.status_code < 400:
                base_url = test_url
                break
        except requests.RequestException:
            pass

    if base_url is None:
        pass

# port
    for port in range(0, 10000):
        try:
            url = f"{base_url}:{port}"
            r = requests.get(url, timeout=3)
            if 200 <= r.status_code < 400:
                print(f"Port: {port}")
                break
        except requests.RequestException:
            pass

    used = True 
    if not  used:
        help()
#completed at 17:22 in 19/12/2025
#by RootWolf
def founction_y():
    global demand
    while True:  # 
        global demand
        start()
        if 'help' in demand:
            help()
        elif demand == 'exit':
            print('Thanks for using ynet!!')
            break 

        else:
            Tool()
