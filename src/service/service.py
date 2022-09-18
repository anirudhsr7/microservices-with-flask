import imp


import socket

class Service:
    def fetchSystemDetails():
        hostname = socket.gethostname()
        host_ip = socket.gethostbyname(hostname)
        return str(hostname), str(host_ip)
