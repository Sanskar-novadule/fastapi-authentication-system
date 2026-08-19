from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from controllers.jwt_controller import router as jwt_router
from controllers.oauth_controller import router as oauth_router
from controllers.secret_key_controller import router as secret_router

from utils.logger import logger


app = FastAPI(
    title="FastAPI Security CRUD API",
    description="JWT, OAuth2 and Secret Key protected CRUD APIs",
    version="1.0.0"
)


# ============================================================
# GLOBAL EXCEPTION HANDLER
# ============================================================

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    # Log complete exception
    logger.exception(
        "Unhandled exception | Method=%s | Path=%s | Error=%s",
        request.method,
        request.url.path,
        str(exc)
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error"
        }
    )


# ============================================================
# ROUTERS
# ============================================================

app.include_router(jwt_router)
app.include_router(oauth_router)
app.include_router(secret_router)


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    logger.info("Home endpoint called")

    return {
        "message": "FastAPI Security API is running"
    }