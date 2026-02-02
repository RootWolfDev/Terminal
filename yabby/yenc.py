import requests
import socket
import marshal
import py_compile
import shutil
import uncompyle6
import subprocess
import PyObfuscator
from rich import print
from rich.console import Console
#theme
def textascii_yenc():
    print(r"""[green]
                                 
 ___.__. ____   ____   ____  
<   |  |/ __ \ /    \_/ ___\ 
 \___  \  ___/|   |  \  \___ 
 / ____|\___  >___|  /\___  >
 \/         \/     \/     \/ 
    """)
demand=None
def line_e():
    terminal_width = shutil.get_terminal_size().columns
    print("-" * terminal_width)
def start_e():
     global demand
     console = Console()
     demand = console.input("([red]yabby_enc[/])> ")
     return demand
def help_e():
   print('__encripting__')
   print('always start with yenc')
   print('to run this tool true create a file and when he want the path of new fle give him !')
   documentation_e={'marshel code':'-Mc',
          'marshel decode':'-Md',
          'bytecode encripting pyc':'-Be',
          'bytecode unencripting pyc':'-Bu',
          'Anonymous encripting':'-Ae'
          }
   for key, value in documentation_e.items():
      print(f'[red]{key}[/]:[green]{value}[/]')
def Tool_e():
   global demand
   result_e = demand

    # Encode Python file to binerie
   if   result_e == 'yenc -Mc':
      line_e()
      file1 = input('PATH_FILE (.py): ')
      file2 = input('PATH_NEW_FILE (.bin): ')
        
      try:
         with open(file1, 'r', encoding='utf-8') as f:
               code = f.read()
            
            #
         compiled_code = compile(code, '<string>', 'exec')
            
            
         with open(file2, 'wb') as f2:
            f2.write(marshal.dumps(compiled_code))
            
            print('Successfully completed!')

      except FileNotFoundError:
         print('[red]error:[/] file not found ')
      except Exception as e:
         print(f'[red]error:[/] {e}')

    # Decode binerie to python there is some broblem here
   elif result_e == 'yenc -Md':
      line_e()
      file1 = input('PATH_FILE (.bin): ')
      file2 = input('PATH_NEW_FILE (.py): ')
        
      try:
         with open(file1, 'rb') as f:
            obj = marshal.load(f)
            
         with open(file2, 'wb') as f2:
            f2.write(marshal.dumps(obj))
            
         print('Successfully completed!')

      except FileNotFoundError:
         print('[red]error:[/] file not found')
      except EOFError:
         print('[red]error:[/] in file')
      except Exception as e:
         print(f'[red]error:[/]  {e}')
   elif  result_e ==' yenc -Be' :
      line_e()
      file1 = input('PATH_FILE (.py): ')
      file2 = input('PATH_NEW_FILE (.pyc): ')
      try:
         with open(file1, 'r', encoding='utf-8') as f:
            py_compile.compile(file1,cfile=file2)
            print('Successfully completed!')
      except FileNotFoundError:
         print('[red]error:[/] file not found ')
      except Exception as e:
         print(f'[red]error:[/] {e}')
   elif result_e == 'yenc -Bu':
      try:
         file1 = input('PATH_FILE (.pyc): ')
         file2 = input('PATH_NEW_FILE (.py): ')
         with open(file2, 'w') as f_out:
            uncompyle6.decompile_file(file1, f_out)
            print('Successfully completed!')
      except FileNotFoundError:
         print('[red]error:[/] file not found ')
      except Exception as e:
         print(f'[red]error:[/] {e}')
   elif result_e == 'yenc -Ae':
      try:
         file1 = input('PATH_FILE (.py): ')
         file2 = input('PATH_NEW_FILE (.py): ')

         cmd = [
            'py', '-m', 'PyObfuscator',
            '-o', file2,
            file1
        ]

         result = subprocess.run(cmd, capture_output=True, text=True)
         print("stdout:\n", result.stdout)
         print("stderr:\n", result.stderr)

         if result.returncode == 0:
            print('Successfully completed!')
         else:
            print('failed!')
      except Exception as e:
         print(f"[red]error:[/] {e}")
   else:
       print('[red]error![/]')
def founction_e():
   global demand
   while True:  # 
        start_e()
        if 'help' in demand:
            help_e()
        elif demand == 'exit':
            print('Thanks for using yenc!!')
            break 
        else:
            Tool_e()