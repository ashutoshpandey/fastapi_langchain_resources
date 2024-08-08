from fastapi import APIRouter
from services.resource_serv import process_query

router = APIRouter()

@router.get("/resource/{query}")
async def query(query: str):
    response = await process_query(query)
    return { "response": response }
