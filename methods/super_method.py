from modules import *
class Super_method:
    def __init__(
        self,
        url : str,
        headers : dict,
        METHOD:str,
        payload=None,
        ) -> None:
        self.url = url
        self.weburl = url.split("://")[1:2][0].split("/")[0]
        self.path = url.split("://")[1].split("/")
        self.request= Headers(
            PATH=self.path,
            METHOD=METHOD,
            URL=self.weburl,
            HEADERS=headers,
            payload=payload,
            ).create_headers()
        self.sock , self.port = Request_obj(url=self.url).Create_socket_OBJ()
        self.Sockheader = Sock_settings(self.sock)
        self.sock.connect((self.weburl,self.port))
        self.Sockheader.send_all(data=bytes(self.request,"UTF-8"))
        self.response = self.Sockheader.recv_all(bytes=4069)
        self.status_c = self.Sockheader.status_code()
        self.sock.close()
        
    @property
    def status_code(self):
        return self.status_c
    
    @property
    def return_all(self):
        return self.completion