from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse

from app.api.mini_wallet.initialize_account import initialize_account
from app.api.mini_wallet.enable_account import enable_account
from app.api.mini_wallet.view_balance import view_balance
from app.api.mini_wallet.add_virtual_money import add_virtual_money
from app.api.mini_wallet.use_virtual_money import use_virtual_money
from app.api.mini_wallet.disable_account import disable_account

from app.utils.dependency import JWTBearer

def alive():
    return 'alive'


router = APIRouter()

router.add_api_route('/alive', endpoint=alive, tags=['Status'], response_class=PlainTextResponse)

router.add_api_route('/init', endpoint=initialize_account, methods=['POST'], tags=['miniWallet'], response_description='Check Version (POST)')
router.add_api_route('/wallet', endpoint=enable_account, methods=['POST'], tags=['miniWallet'], response_description='Check Version (GET)', dependencies=[Depends(JWTBearer(login_required=False))])
router.add_api_route('/wallet', endpoint=view_balance, methods=['GET'], tags=['miniWallet'], response_description='Check Version (GET)', dependencies=[Depends(JWTBearer(login_required=False))])
router.add_api_route('/wallet/deposits', endpoint=add_virtual_money, methods=['POST'], tags=['miniWallet'], response_description='Check Version (GET)', dependencies=[Depends(JWTBearer(login_required=False))])
router.add_api_route('/wallet/withdrawals', endpoint=use_virtual_money, methods=['POST'], tags=['miniWallet'], response_description='Check Version (GET)', dependencies=[Depends(JWTBearer(login_required=False))])
router.add_api_route('/wallet', endpoint=disable_account, methods=['PATCH'], tags=['miniWallet'], response_description='Check Version (GET)', dependencies=[Depends(JWTBearer(login_required=False))])