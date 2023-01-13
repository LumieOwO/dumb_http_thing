from modules import *
class Post:
    def __init__(
            self,
            url : str,
            headers : dict,
            payload: dict
            ) -> None:
        self.url = url
        self.weburl = url.split("://")[1:2][0].split("/")[0]
        self.path = url.split("://")[1].split("/")
        temp = {
            "Content-Type":"Application/json"
        }
        header = headers.update(temp)
        self.request= Headers(
            PATH=self.path,
            METHOD="POST",
            URL=self.weburl,
            HEADERS=headers,
            payload=payload
            ).create_headers()
        self.sock , self.port = Request_obj(url=self.url).Create_socket_OBJ()
        self.Sockheader = Sock_settings(self.sock)
        self.sock.connect((self.weburl,self.port))
        self.Sockheader.send_all(data=bytes(self.request,"UTF-8"))
        self.response = self.Sockheader.recv_all(bytes=4069)
        self.status_c = self.Sockheader.status_code()
        self.sock.close()
        self.completion = Completion_util(self.response,self.status_c,self.Sockheader.text(dat=self.response))


    def return_all(self):
        return self.completion
        
if __name__ == '__main__':
    url = "http://data.pr4e.org/romeo.txt"
    main = Post(url=url)
    input()