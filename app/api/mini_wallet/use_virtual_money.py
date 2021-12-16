from fastapi import Request

from app.utils.response import JsonResponse
from app.utils.logger import logger

from pydantic import BaseModel
from datetime import datetime

class Whitdrawn(BaseModel):
    amount : int
    reference_id : str

async def use_virtual_money(request : Request, whitdrawn : Whitdrawn):
    try:
        decodeToken = request.state.payload
    except:
        logger.warning('Authorization Failed')

        return JsonResponse(data = {},  status = 'Authorization Required', status_code = 401)

    if not whitdrawn.reference_id or not whitdrawn.amount or not decodeToken:
        return JsonResponse(data = {},  status = 'Unauthorized', status_code = 401)
    
    decodeToken["withdrawal"]["reference_id"] = whitdrawn.reference_id
    decodeToken["withdrawal"]["amount"] = whitdrawn.amount
    decodeToken["withdrawal"]["whitdrawn_at"] = str(datetime.now())
    
    return JsonResponse(data = decodeToken,  status = 'Success', status_code = 201)