from fastapi import APIRouter
from services.resource_serv import get_resource_response

router = APIRouter()

@router.get("/resource/{query}")
async def query(query: str):
    response = await get_resource_response(query)
    return { "response": response }
