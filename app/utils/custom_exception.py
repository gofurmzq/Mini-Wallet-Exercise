import typing


class TokenException(Exception):
    def __init__(self, data: typing.Any = None, message: str = None, status_code: int = 200, code: int = None,
                 success: bool = False):
        self.data = data
        self.message = message
        self.status_code = status_code
        self.code = code
        self.success = success
