from fastapi import APIRouter
from services.cv_serv import get_cv_response

router = APIRouter()

@router.get("/cv/{query}")
async def query(query: str):
    response = await get_cv_response(query)
    return { "response": response }