class Completion_util:
    def __init__(
            self,
            response,
            status_c,
            text=None
            ) -> None:
        self.response = response
        self.status_code = status_c
        self.text = text