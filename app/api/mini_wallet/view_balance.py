from logging import exception
from fastapi import Request

from app.utils.response import JsonResponse
from app.config import settings
from app.utils.logger import logger

async def view_balance(request : Request):
    try:
        decodeToken = request.state.payload
    except:
        logger.warning('Authorization Failed')

        return JsonResponse(data = {},  status = 'Authorization Required', status_code = 401)


    logger.info(f'success enable with info account {str(decodeToken)}')

    return JsonResponse(data = decodeToken,  status = 'Success', status_code = 201)