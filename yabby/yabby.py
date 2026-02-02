import random
import yirb
import ynet
import yenc
import os
from rich.console import Console
from rich import print 
def banner():
    banners=[r"""[red]
      ___           ___           ___           ___           ___              
     |\__\         /\  \         /\  \         /\  \         |\__\             
     |:|  |       /::\  \       /::\  \       /::\  \        |:|  |            
     |:|  |      /:/\:\  \     /:/\:\  \     /:/\:\  \       |:|  |            
     |:|__|__   /::\~\:\  \   /::\~\:\__\   /::\~\:\__\      |:|__|__          
     /::::\__\ /:/\:\ \:\__\ /:/\:\ \:|__| /:/\:\ \:|__|     /::::\__\         
    /:/~~/~    \/__\:\/:/  / \:\~\:\/:/  / \:\~\:\/:/  /    /:/~~/~            
   /:/  /           \::/  /   \:\ \::/  /   \:\ \::/  /    /:/  /              
   \/__/            /:/  /     \:\/:/  /     \:\/:/  /     \/__/               
                   /:/  /       \::/__/       \::/__/                          
                   \/__/         ~~            ~~                              
   [/] """,
    r"""[blue]
     _        _          _                   _               _    _        _    
/\ \     /\_\       / /\                / /\            / /\ /\ \     /\_\  
\ \ \   / / /      / /  \              / /  \          / /  \\ \ \   / / /  
 \ \ \_/ / /      / / /\ \            / / /\ \        / / /\ \\ \ \_/ / /   
  \ \___/ /      / / /\ \ \          / / /\ \ \      / / /\ \ \\ \___/ /    
   \ \ \_/      / / /  \ \ \        / / /\ \_\ \    / / /\ \_\ \\ \ \_/     
    \ \ \      / / /___/ /\ \      / / /\ \ \___\  / / /\ \ \___\\ \ \      
     \ \ \    / / /_____/ /\ \    / / /  \ \ \__/ / / /  \ \ \__/ \ \ \     
      \ \ \  / /_________/\ \ \  / / /____\_\ \  / / /____\_\ \    \ \ \    
       \ \_\/ / /_       __\ \_\/ / /__________\/ / /__________\    \ \_\   
        \/_/\_\___\     /____/_/\/_____________/\/_____________/     \/_/   
                                                                            
    [/]""",
    r"""[green]
                  ('-.    .-. .-') .-. .-')                    
             ( OO ).-.\  ( OO )\  ( OO )                   
  ,--.   ,--./ . --. / ;-----.\ ;-----.\  ,--.   ,--.      
   \  `.'  / | \-.  \  | .-.  | | .-.  |   \  `.'  /       
 .-')     /.-'-'  |  | | '-' /_)| '-' /_).-')     /        
(OO  \   /  \| |_.'  | | .-. `. | .-. `.(OO  \   /         
 |   /  /\_  |  .-.  | | |  \  || |  \  ||   /  /\_        
 `-./  /.__) |  | |  | | '--'  /| '--'  /`-./  /.__)       
   `--'      `--' `--' `------' `------'   `--'            
    [/]""",
    r"""[yellow]
         )                       
  ( /(         )    )        
  )\())   ) ( /( ( /( (      
 ((_)\ ( /( )\()))\()))\ )   
__ ((_))(_)|(_)\((_)\(()/(   
\ \ / ((_)_| |(_) |(_))(_))  
 \ V // _` | '_ \ '_ \ || |  
  |_| \__,_|_.__/_.__/\_, |  
                      |__/   
    [/]""",
    r"""[purple]
      __  __    _____     _____    _____    __  __    
/\  /\  /\ /\___/\  /\  __/\ /\  __/\ /\  /\  /\  
\ \ \/ / // / _ \ \ ) )(_ ) )) )(_ ) )\ \ \/ / /  
 \ \__/ / \ \(_)/ // / __/ // / __/ /  \ \__/ /   
  \__/ /  / / _ \ \\ \  _\ \\ \  _\ \   \__/ /    
  / / /  ( (_( )_) )) )(__) )) )(__) )  / / /     
  \/_/    \/_/ \_\/ \/____\/ \/____\/   \/_/      
                                                  
    [/]"""
    ] 
    print(random.choice(banners),' [red]by root wolf[/]')
    print('welcome to Yabby security')
    print('> "set [red]help[/] to show how to use this tool"')
    print('> "set [red]about[/] to know more about us"')
def help_h():
    documentation_h={'using tool':'use (name tool)',
    'show tool and name of it ':'show tool',}
    for key, value in documentation_h.items():
        print(f'[red]{key}[/]:[green]{value}[/]')
def showtool():
    show_t={'ynet':'cheking network',
    'yenc':'encripting file',
    'yirb':'cheking hide and ending points'}
    for key,value in show_t.items():
        print(f'[red]{key}[/]:[green]{value}[/]')
def about():
    print('from  wikipedia:[blue]https://en.wikipedia.org/[/]')
    print('[red]Yabby[/] is a name given in Australia to two different kinds of crustacean:\nCherax (freshwater yabby), a crayfish\n Trypaea (marine yabby), a ghost shrimp (infraorder Thalassinidea) which lives in the intertidal zone')
    print('this is my tool of security build completly with python ')
def home():
    console=Console()
    result_h = console.input("([red]yabby[/])> ").strip()
    if result_h == 'help':
        help_h()
    elif result_h=='show tool':
        showtool()
    elif result_h == 'about':
        about()
        #the 
    elif result_h == 'use yirb':
        yirb.texirb()
        yirb.founction_b()
    elif result_h == 'use ynet':
        ynet.textascii()
        ynet.founction_y()  
    elif result_h == 'use yenc':
        yenc.textascii_yenc()
        yenc.founction_e()
    elif result_h == 'exit':
        exit()
    elif result_h== '' :
        pass
    else:
        print('[red]error![/]')
def founction_h():
    banner()
    while True:
       home()
founction_h()