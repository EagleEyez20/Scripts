
import socket
from datetime import datetime

def scan_ports(host, start_port=1, end_port=1024):
    try:
        # Resolve the hostname to an IP address
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Error resoving host: {host}")
        return
    
    print(f"Scanning {host} ({ip}) from port {start_port} to {end_port}")
    start_time = datetime.now()
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()
        
    end_time = datetime.now()
    total_time = end_time - start_time
    print (f"Scanning completed in (Total_time)")
    
if __name__ == "__main__":
    target = input("Enter the host to scan")
    start_port = input("Enter the start port (default is 1): ")
    end_port = input("Enter the end port (default is 1024): ")

    start_port = int(start_port) if start_port else 1
    end_port = int(end_port) if end_port else 1024
    
    scan_ports(target, start_port, end_port)


