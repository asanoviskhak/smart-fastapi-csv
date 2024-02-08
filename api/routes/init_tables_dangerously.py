from fastapi import APIRouter, status
from db.sessions import create_tables, upload_to_tables

router = APIRouter()

@router.post(  
    "/approve",  
    status_code=status.HTTP_204_NO_CONTENT,  
    name="init_tables"  
)

async def init_tables():  
    create_tables()