from .super_method import Super_method
from modules import Completion_util
class Head(Super_method):
        def __init__(
                    self, 
                    url: str, 
                    headers: dict,
                    ) -> None:
            super().__init__(url, 
                  headers,
                  METHOD="HEAD"
                  )
            self.completion = Completion_util(self.response,self.status_c)

