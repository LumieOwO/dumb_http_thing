from .super_method import Super_method
from modules import Completion_util
class Post(Super_method):
        def __init__(
                    self, 
                    url: str, 
                    headers: dict,
                    payload:dict
                    ) -> None:
            temp = {"Content-Type":"Application/json"}
            header = headers.update(temp)
            super().__init__(url, 
                 headers,
                 METHOD="POST",
                 payload=payload
                 )
            self.completion = Completion_util(self.response,self.status_c)            
        @property
        def text(self):
            return self.Sockheader.text(dat=self.response)