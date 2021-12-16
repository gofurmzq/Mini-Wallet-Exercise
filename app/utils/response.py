import typing
from fastapi.responses import JSONResponse as response_json


def JsonResponse(data: typing.Any = None, status: str = 'Success', status_code: int = 201):

    return response_json({
        'data': data,
        'status': status
    }, status_code=status_code)
