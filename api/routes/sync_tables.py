from fastapi import APIRouter, status
from db.sessions import create_tables, upload_to_tables

router = APIRouter()

@router.get(  
    "",  
    status_code=status.HTTP_204_NO_CONTENT,  
    name="sync_tables"  
)

async def sync_tables():  
    upload_to_tables()