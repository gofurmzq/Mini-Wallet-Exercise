from fastapi import Request

from app.utils.response import JsonResponse
from app.utils.logger import logger
from app.utils.token import encode_jwt

from pydantic import BaseModel

class Token(BaseModel):
    customer_xid : str


async def initialize_account(request : Request, token : Token):
    if not token.customer_xid:
        return JsonResponse(data = {},  status = 'Unauthorized', status_code = 401)
    
    logger.info(f'customer_xid : {token.customer_xid} success initialize account')

    token = encode_jwt({"customer_xid" : token.customer_xid})
    
    return JsonResponse(data = {"token" : token},  status = 'Success', status_code = 201)