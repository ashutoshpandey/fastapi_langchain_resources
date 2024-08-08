from fastapi import FastAPI
from controllers.cv_ctrl import router as cv_router
from controllers.resource_ctrl import router as resource_router

app = FastAPI()

app.include_router(cv_router)
app.include_router(resource_router)
