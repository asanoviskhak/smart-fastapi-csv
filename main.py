from fastapi import FastAPI, status  
import uvicorn
from multiprocessing import cpu_count, freeze_support

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


def start_server(host="127.0.0.1",
                 port=8000,
                 num_workers=2,
                 loop="asyncio",
                 reload=False):
    uvicorn.run("main:app",
                host=host,
                port=port,
                workers=num_workers,
                loop=loop,
                reload=reload)
    
if __name__ == "__main__":
    freeze_support()  # Needed for pyinstaller for multiprocessing on WindowsOS
    num_workers = int(cpu_count() * 0.75)
    start_server(num_workers=num_workers)