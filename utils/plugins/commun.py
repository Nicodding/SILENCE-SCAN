import requests
from colorama import Fore, Back, Style


        

class Colors:
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }

    @classmethod
    def color_text(cls, text, color):
        if color not in cls.colors:
            raise ValueError('Invalid color')
        return cls.colors[color] + text + cls.colors['reset']

class Ascii:
    @classmethod
    
    def banner(cls, user):
        print(f"""{Fore.RED}            
╔═╗╦╦  ╔═╗╔╗╔╔═╗╔═╗  ╔╗╔╔═╗╔╦╗╦ ╦╔═╗╦═╗╦╔═
╚═╗║║  ║╣ ║║║║  ║╣   ║║║║╣  ║ ║║║║ ║╠╦╝╠╩╗
╚═╝╩╩═╝╚═╝╝╚╝╚═╝╚═╝  ╝╚╝╚═╝ ╩ ╚╩╝╚═╝╩╚═╩ ╩
{Fore.RESET}

Version: 1.0.0
Author: TryWarz
Github: https://github.com/Nicodding
                                                        
                                """)
    def help():
        print(
        """
Usage: [option]
-s, --scanport: Scan port
-e, -exit: Exit
-c, -clear: Clear screen
-h, -help: Help
        """)
    