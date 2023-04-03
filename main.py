import time
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from utils.dbUtil import database
from topic import router as topic_router


from exceptions.business import BusinessException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="FastAPI (python)",
    description="FastAPI framework",
    version="1.0",
    openapi_url="/openapi.json",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
 )

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    request.state.connection = database
    response = await call_next(request)
    start_time = time.time()
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)

    return response


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.exception_handler(BusinessException)
async def business_exception_handler(request: Request, e: BusinessException):
    return JSONResponse(
        status_code=418,
        content={"code": e.status_code, "message": e.detail},
    )

app.include_router(topic_router.topic, tags=["Topic"])


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
