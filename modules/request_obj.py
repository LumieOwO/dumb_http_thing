import socket
import ssl

class Request_obj:

    def __init__(
            self,
            url : str
            ) -> None:
        self.url = url
        self.port = self.get_port(url=self.url)

    def Create_socket_OBJ(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(30)
        """ssl.SSLContext().wrap_socket(sock=sock)""" 
        if self.port == 443:
            return ssl.SSLContext().wrap_socket(sock=sock, server_hostname=self.url.split('/')[2]), self.port
        elif self.port == 80:
            sock = sock
            return sock, self.port
        else:
            exit()
        
        
    def get_port(self,url) -> int or str:
        if url.split("://")[0] == "https":
            return 443
        elif url.split("://")[0] == "http":
            return 80
        else:
            return "unknown SCHEME"
