import os
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            access_key = os.getenv('ACCESS_KEY')
            secret_key = os.getenv('SECRET_KEY')

            # Retrieve headers
            request_secret_key = request.headers.get('SECRET_KEY')
            request_access_key = request.headers.get('ACCESS_KEY')

            # Validate keys
            if not request_secret_key or not request_access_key:
                raise HTTPException(status_code=400, detail="Missing SECRET_KEY or ACCESS_KEY in headers")

            if request_secret_key != secret_key or request_access_key != access_key:
                raise HTTPException(status_code=403, detail="Invalid SECRET_KEY or ACCESS_KEY")

            # Proceed to the next middleware or endpoint
            response = await call_next(request)
            return response
        except Exception as e:
            return JSONResponse(
                status_code=400,
                content={"error": "You are not authorized to access the api"}
            )