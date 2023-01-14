from .super_method import Super_method
from modules import Completion_util
class Options(Super_method):
        def __init__(
                    self, 
                    url: str, 
                    headers: dict,
                    ) -> None:
            super().__init__(url, 
                  headers,
                  METHOD="OPTIONS"
                  )
            self.completion = Completion_util(self.response,self.status_c)

        @property
        def Allowed_METHODS(self):
            return self.Sockheader.allowed_METHODS(dat=self.response)


