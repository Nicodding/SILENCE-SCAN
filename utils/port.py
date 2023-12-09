import socket
import threading
import time
from colorama import Fore


PORT_SERVICES = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    465: 'SMTPS',
    587: 'SMTP',
    993: 'IMAPS',
    995: 'POP3S',
    3306: 'MySQL',
    5432: 'PostgreSQL',
    8080: 'HTTP Proxy'
}


class Configuration:
    """
    Represents a configuration for port scanning.

    Attributes:
        ip_address (str): The IP address to scan.
        start_port (int): The starting port number (default is 1).
        end_port (int): The ending port number (default is 65535).
        timeout (float): The timeout value in seconds (default is 0.04).
    """

    def __init__(self, ip_address, start_port=1, end_port=65535, timeout=0.04):
        self.ip_address = ip_address
        self.start_port = start_port
        self.end_port = end_port
        self.timeout = timeout

    def scan_ports(self):
        """
        Scans the ports within the specified range and prints the open ports.

        Returns:
            list: A list of tuples containing the open ports and their corresponding service names.
        """
        open_ports = []
        threading.Thread(target=self.loading).start()
        for port in range(self.start_port, self.end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.ip_address, port))
                if result == 0:
                    service_name = PORT_SERVICES.get(port, 'Unknown')
                    open_ports.append((port, service_name))
                    print(f'[-] PORT OPEN: {port} ({service_name})                                                                    ', end='\n\r')

    def loading(self):
        """
        Displays a loading progress bar while scanning the ports.
        """
        total_ports = self.end_port - self.start_port + 1
        for port in range(self.start_port, self.end_port + 1):
            time.sleep(self.timeout)
            percentage = (port / self.end_port) * 100
            loading = int(percentage / 2)
            remaining_ports = total_ports - port
            remaining_time = remaining_ports * self.timeout
            print(f"{Fore.RED}[{Fore.GREEN}{'=' * loading}{' ' * (50 - loading)}{Fore.RED}] {Fore.GREEN}{percentage:.2f}% - Remaining Time: {remaining_time:.2f}s\r", end="")
