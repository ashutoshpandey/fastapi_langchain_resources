import os
from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager

from controllers.cv_ctrl import router as cv_router
from utils.cache_util import load_csv_data, load_pdf_data
from controllers.resource_ctrl import router as resource_router

app = FastAPI()

app.include_router(cv_router)
app.include_router(resource_router)

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()

    cv_path = os.getenv('CV_PATH')
    resource_path = os.getenv('RESOURCE_PATH')

    print(cv_path, " , ", resource_path)

    # Load data at startup
    #await load_pdf_data('../' + cv_path)
    await load_csv_data('../' + resource_path)

    print("Data loaded")

    yield

    print("Shutting down application")


app.router.lifespan_context = lifespan
