from fastapi import FastAPI, status  
  
from core.config import settings  
from api.router import router  
from db.sessions import create_tables, upload_to_tables

  
app = FastAPI(  
    title=settings.title,  
    version=settings.version,  
    description=settings.description,  
    openapi_prefix=settings.openapi_prefix,  
    docs_url=settings.docs_url,  
    openapi_url=settings.openapi_url  
)  
  
app.include_router(router, prefix=settings.api_prefix)  
  
  
@app.get("/")  
async def root():  
    return {"Say": "Hello!"}  
  
@app.get("/check_system", status_code=status.HTTP_200_OK)
def check_system():  
    return "OK"
