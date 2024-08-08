from fastapi import FastAPI
from services.cv_serv import get_cv_response
from services.resource_serv import get_resource_response

app = FastAPI()

@app.get("/resource/{query}")
async def query(query: str):
    response = await get_resource_response(query)
    return { "response": response }


@app.get("/cv/{query}")
async def query(query: str):
    response = await get_cv_response(query)
    return { "response": response }