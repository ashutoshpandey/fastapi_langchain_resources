from fastapi import FastAPI
from services.resource_serv import get_query_response

app = FastAPI()

@app.get("/query/{query}")
async def query(query: str):
    response = await get_query_response(query)
    return { "response": response }