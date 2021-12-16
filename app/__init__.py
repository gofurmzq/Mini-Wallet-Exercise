from app.config import settings

import typing

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exceptions import RequestValidationError

from app.utils.logger import MyFilter, logger, _log_format
from logging import StreamHandler
from logging.handlers import WatchedFileHandler

from app.api import router
from app.utils.custom_exception import TokenException
from app.utils.response import JsonResponse
from app.version import API_VERSION, API_NAME, VERSION


if settings.LOG_TO_FILE:
    stream_handler = StreamHandler()
    stream_handler.setLevel(settings.LOG_LEVEL_INFO)
    stream_handler.setFormatter(_log_format)
    logger.addHandler(stream_handler)

    for i in range(len(settings.LOG_FILE)):
        file_handler = WatchedFileHandler(settings.LOG_FILE[i])
        file_handler.setLevel(settings.LOG_LEVEL[i])
        file_handler.addFilter(MyFilter(settings.LOG_LEVEL[i]))
        file_handler.setFormatter(_log_format)
        logger.addHandler(file_handler)
    logger.setLevel(settings.LOG_LEVEL_INFO)

app_kwargs = dict(
    docs_url=f'/api/{API_VERSION}/wallet/docs',
    redoc_url=f'/api/{API_VERSION}/wallet/redoc',
    openapi_url=f'/api/{API_VERSION}/wallet/openapi.json'
)

if not settings.ENABLE_APIDOCS:
    app_kwargs.update(dict(docs_url=None, redoc_url=None))

app = FastAPI(**app_kwargs, title=API_NAME, version=VERSION)

@app.middleware('http')
async def cors_middleware(request: Request, call_next):
    cors_headers = {
        'Access-Control-Allow-Origin': settings.CORS_ALLOW_ORIGINS,
        'Access-Control-Allow-Methods': settings.CORS_ALLOW_METHODS,
        'Access-Control-Allow-Headers': settings.CORS_ALLOW_HEADERS
    }

    if request.method == 'OPTIONS':
        return Response(
            status_code=204,
            headers=cors_headers
        )

    response = await call_next(request)
    response.headers.update(cors_headers)

    return response


@app.exception_handler(TokenException)
async def TokenExceptionHandler(request: Request, exc: TokenException):
    return JsonResponse(
        status=exc.message,
        status_code=exc.status_code,
    )

@app.exception_handler(HTTPException)
async def handle_http_exception(request: Request, exc: HTTPException):
    message: str = exc.detail
    code: int = exc.status_code
    status_code: int = code

    return JsonResponse(
        status=message,
        status_code=status_code,
    )


@app.exception_handler(RequestValidationError)
async def handle_validation_error(request: Request, exc: RequestValidationError):
    error_list: typing.List[dict] = exc.errors()
    error_messages: dict = {}
    for error in error_list:
        if len(error['loc']) < 2:
            return JsonResponse(
                status='Please check your data',
                status_code=400
            )

        error_messages.update(
            {error['loc'][1]: error['msg']}
        )

    return JsonResponse(
        data=error_messages,
        status='Please check your data',
        status_code=400
    )


app.include_router(router, prefix=f'/api/{API_VERSION}')
