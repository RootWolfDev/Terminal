from rich import print
import time
import sys
import subprocess
import os
import getpass
#import build_html
from rich.console import Console
def wolfascii():
    print(r"""
                             ___________
                    __.-' `     `  ``--.___
 VK               .'.        `     `  `    `-.___
                 / -                   ` `  ` `  `--.
                / -                    -       `  `  `-.
               /_ -        '           .-           . ` `.  .-.
              /         |             - -'      `  / \  ` `// |
             /      `       '        -        `   ||\ `   //  |
           .'           |       '    -            || |'    `' '
         .'-       `    |  |  |    -   .     -  //       |    '
       .' -     `                     .         /       ` .-  `
     .'   - '      `   /.|'`.   |   /        /       ` o ||o' `
    J     )  '        /'  ``|`|    /         /  /       `||'.'
    |__.-'7'       .-'  \ `   ``.       |     / / /  .  '|||
      _.-'      .-'      \` '   /`.     \ ___  / '.  \\  |||
     /     __.-'         | '   /  |     |    `-----'-.\\ ( )
    /   .-'              J    /   |     |      |       \`-<
   /   /                 F   J     \    |       \       `-'
  /   /                 /   |       |   |        `-._     )
 |   /                 (    |       | \ )            `.   |
-`---`--------.---------`.   `.     \   \             /'  |   __| |   |
  .-.___`-.___ `._   ---. `.   `.___ \   \           |   /   (    |   |
 ------    `---._    `------\_____)_\_\   \_          \='|  \_ _|\__,_|
 __.-.      --.        `-----.____    '._/__`._  ___   \=/   _/       _
    .--           -.  -                        `-   `------.--.__.---'
------------------------------------------------
Thank you for visiting https://asciiart.website/
This ASCII pic can be found at
https://asciiart.website/art/784
    """)
    print('welcome to wolf terminal ')
    print('> "set [red]list[/] to show tools"')
    print('> "set [red]help[/] to help you"')
ke=None

    
def login():#wolf wolf
    global ke
    ke = False  # initialize the global variable
    attempts = 0
    user_key = 'wolf'
    pass_key = 'wolf'

    while attempts < 3:
        username = getpass.getpass('username: ')
        password = getpass.getpass('password: ')

        if username == user_key and password == pass_key:
            print("Login successful!")
            ke = True
            break  # exit the loop if login is correct
        elif username == user_key and password != pass_key:
            print('Incorrect password!')
        elif username != user_key and password == pass_key:
            print('Incorrect username!')
        else:
            print('Error!')

        attempts += 1

    if not ke:
        print("Too many failed attempts. Exiting...")
        exit()
def loading_animation(duration=5):
    anim = ["*", "/*", "/*/", "*/", "*/", "/*", "/*/"]
    start_time = time.time()

    while time.time() - start_time < duration:
        for frame in anim:
            if time.time() - start_time >= duration:
                break
            sys.stdout.write("\r[*] Loading " + frame)
            sys.stdout.flush()
            time.sleep(0.2)

    print("\n")    
def help_w():
     documentation_w={'to use any tool write':'(name tool)',
     'to show the tool list in this terminal write':'list'}
     for key, value in documentation_w.items():
        print(f'[red]{key}[/]:[green]{value}[/]')
def list_w():
    list_w={'post':'buil a html page',
    'yabby':'tool for hacking network',
    'octopus':'librery of tool hacking'}
    for key, value in list_w.items():
        print(f'/*/[red]{key}[/]:[green]{value}[/]')
def menu():
    console=Console()
    result_w = console.input(r"""  [red]----------------[/]([purple]T[/][red]@[/][purple]wolf[/])
[red] |[/]
  [red]----------# [/]""")
    if result_w == 'help':
        help_w()
    elif result_w == 'list':
        list_w()
    #tool function
    elif result_w =='yabby':
        current_dir = os.path.dirname(os.path.abspath(__file__))
        target_file = os.path.join(current_dir, "yabby", "yabby.py")
        subprocess.run(["python", target_file])
   # elif result_w == 'html':
    #    build_html.first()
    elif result_w == 'octopus':
        current_dir = os.path.dirname(os.path.abspath(__file__))
        target_file = os.path.join(current_dir, "octopus", "chatbot.py")
        subprocess.run(["python", target_file])
    elif result_w == 'html':
    #if you add another converter add a list to them
        current_dir = os.path.dirname(os.path.abspath(__file__))
        target_file = os.path.join(current_dir, "converter", "htmlconv.py")
        subprocess.run(["python", target_file])
    elif result_w == 'exit':
        exit()
    elif result_w == 'clear':
        os.system('cls')
    elif result_w == '' :
        pass
    else:
        print('[red]error![/]')
def founction_c():
    login()
    global ke
    if ke==True:
        loading_animation(duration=5)
        wolfascii()
        while True :
            menu()
    else:
        pass
founction_c() #what now