from fastapi import APIRouter

from api.routes.sync_tables import router as sync_tables_router
from api.routes.init_tables_dangerously import router as init_tables_dangerously_router

router = APIRouter()

router.include_router(sync_tables_router, prefix="/sync_tables")
router.include_router(init_tables_dangerously_router, prefix="/init_tables_dangerously")