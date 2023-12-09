import os
import socket
import getpass
from utils.port import *
from utils.plugins.commun import *


class Silence:
    def __init__(self):
        self.user = getpass.getuser()

    def commande(self):
        try:
            choice = input(
                f"{Fore.BLACK + Style.BRIGHT}{self.user}{Style.RESET_ALL}{Fore.RED + Style.NORMAL} ⭑ Silence > {Style.RESET_ALL}"
            ).lower()


            match choice:
                case "-s" | "--scanport":
                    ip_address = input(Colors.color_text("IP: ", "red"))
                    Configuration(
                        ip_address=ip_address,
                        start_port=1,
                        end_port=1000,  # 65535
                        timeout=0.04,
                    ).scan_ports()
                case "-exit" | "-e":
                    print(Colors.color_text("Bye bye", "red"))
                    exit()
                case "-clear" | "-c":
                    os.system("cls")
                    Ascii.banner(user=getpass.getuser())
                    self.commande()
                case "-help" | "-h":
                    Ascii.help()
                case _:
                    raise ValueError("invalid command")

        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

        except KeyboardInterrupt:
            print("\n")
            print(Colors.color_text("Bye bye", "red"))
            exit()


if __name__ == "__main__":
    os.system("title Silence")
    os.system("cls")
    Ascii.banner(user=getpass.getuser())
    main = Silence()
    while True:
        main.commande()
