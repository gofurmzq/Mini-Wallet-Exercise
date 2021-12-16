from fastapi import Request

from app.utils.response import JsonResponse
from app.utils.logger import logger

from pydantic import BaseModel

class Disable(BaseModel):
    is_disabled : str 

async def disable_account(request : Request, disable : Disable):
    try:
        decodeToken = request.state.payload
    except:
        logger.warning('Authorization Failed')

        return JsonResponse(data = {},  status = 'Authorization Required', status_code = 401)

    if not disable.is_disabled or not decodeToken:
        return JsonResponse(data = {},  status = 'Unauthorized', status_code = 401)
    
    if disable.is_disabled == 'true':
        decodeToken["wallet"]["status"] = "disabled"
    else:
        decodeToken["wallet"]["status"] = "enable"

    return JsonResponse(data = decodeToken,  status = 'Success', status_code = 201)