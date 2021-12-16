from fastapi import Request

from app.utils.response import JsonResponse
from app.utils.logger import logger

from pydantic import BaseModel
from datetime import datetime
class Deposit(BaseModel):
    amount : int
    reference_id : str

async def add_virtual_money(request : Request, deposit : Deposit):
    try:
        decodeToken = request.state.payload
    except:
        logger.warning('Authorization Failed')

        return JsonResponse(data = {},  status = 'Authorization Required', status_code = 401)

    if not deposit.reference_id or not deposit.amount or not decodeToken:
        return JsonResponse(data = {},  status = 'Unauthorized', status_code = 401)
    
    decodeToken["deposit"]["reference_id"] = deposit.reference_id
    decodeToken["deposit"]["amount"] = deposit.amount
    decodeToken["deposit"]["deposited_at"] = str(datetime.now())

    return JsonResponse(data = decodeToken,  status = 'Success', status_code = 201)