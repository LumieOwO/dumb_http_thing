class Sock_settings:
    def __init__(
            self,
            socket
            ) -> None:
        self.sock = socket
    def send_all(
            self,
            data,
    ):
        sent    = 0
        while sent < len(data):
            sent = sent + self.sock.send(data[sent:])

    def text(
            self,
            dat):
        data = dat.split("\n")
        lol = 0
        temp = ""
        for i in data:
            if lol == 1:
                temp += f"{i}\n"
            if i == '\r':
                lol = 1
    
        return temp

    def recv_all(
            self,
            bytes
            ):
        self.response = b""

        while True:
            chunk = self.sock.recv(bytes)
  
            if len(chunk) == 0:
                break
            self.response = self.response + chunk

        return self.response.decode()
    


    def status_code(
            self,
            ):
        respons = self.response.decode().partition('\n')[0]
        s_code = [int(i) for i in respons.split() if i.isdigit()][0]
        return s_code