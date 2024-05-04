import platform
import socket

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def get_username():
    return None

def get_ip_address():
    ip_address = socket.gethostbyname(socket.gethostname())
    return ip_address

def get_os_info():
    os_name = platform.platform()
    os_release = platform.release()
    os_version = platform.version()
    install_date = None
    return os_name, os_release, os_version, install_date