import os
import socket
import getpass
from utils.port import *
from utils.plugins.commun import *


class Silence:
    """
    The Silence class represents a command-line tool for scanning ports on a given IP address.

    Attributes:
        user (str): The username of the current user.

    Methods:
        run(): Starts the Silence tool and enters the command loop.
        command(): Handles user commands and executes corresponding actions.
        scan_ports(): Scans ports on a specified IP address.
    """

    def __init__(self):
        self.user = getpass.getuser()

    def run(self):
        """
        Starts the Silence tool and enters the command loop.
        """
        os.system("title Silence")
        os.system("cls")
        Ascii.banner(user=self.user)
        while True:
            self.command()

    def command(self):
        """
        Handles user commands and executes corresponding actions.
        """
        try:
            choice = input(
                f"{Fore.BLACK + Style.BRIGHT}{self.user}{Style.RESET_ALL}{Fore.RED + Style.NORMAL} ⭑ Silence > {Style.RESET_ALL}"
            ).lower()

            if choice in ["-s", "--scanport"]:
                self.scan_ports()
            elif choice in ["-exit", "-e"]:
                print(Colors.color_text("Bye bye", "red"))
                exit()
            elif choice in ["-clear", "-c"]:
                os.system("cls")
                Ascii.banner(user=self.user)
            elif choice in ["-help", "-h"]:
                Ascii.help()
            else:
                raise ValueError("Invalid command")

        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    def scan_ports(self):
        """
        Scans ports on a specified IP address.
        """
        ip_address = input(Colors.color_text("IP: ", "red"))
        Configuration(
            ip_address=ip_address,
            start_port=1,
            end_port=65535,
            timeout=0.04,
        ).scan_ports()


if __name__ == "__main__":
    main = Silence()
    main.run()
