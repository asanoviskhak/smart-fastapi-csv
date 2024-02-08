from sqlmodel import Field, SQLModel
from datetime import datetime
from db.tables.base_class import UUIDModel

class ManagerReportBase(SQLModel):
    MASTER_VALUE_ORDER: int = Field(nullable=False)
    MASTER_VALUE: str = Field(nullable=True)
    RESORT: str = Field(nullable=False)
    CS_HEADING_COUNT_MASTER: int = Field(nullable=False)
    CS_FS_ARR_ROOMS_MASTER: str = Field(nullable=True)
    CS_FS_DEP_ROOMS_MASTER: str = Field(nullable=True)
    CS_FS_NO_ROOMS_MASTER: str = Field(nullable=True)
    CS_FS_GUESTS_MASTER: str = Field(nullable=True)
    CS_FS_TOTAL_REVENUE_MASTER: str = Field(nullable=True)
    CS_FS_ROOM_REVENUE_MASTER: str = Field(nullable=True)
    CS_FS_INVENTORY_ROOMS_MASTER: str = Field(nullable=True)
    CF_FS_PERC_OCC_ROOMS_MASTER: int = Field(nullable=False)
    CF_FS_AVG_ROOM_RATE_MASTER: str = Field(nullable=True)
    CS_FS_OO_ROOMS_MASTER: str = Field(nullable=True)
    LAST_YEAR_01: int = Field(nullable=False)
    SUB_GRP_1_ORDER: int = Field(nullable=False)
    SUB_GRP_1: str = Field(nullable=False)
    DESCRIPTION: str = Field(nullable=True)
    AMOUNT_FORMAT_TYPE: str = Field(nullable=True)
    PRINT_LINE_AFTER_YN: str = Field(nullable=False)
    HEADING_1_ORDER: int = Field(nullable=False)
    HEADING_1: int = Field(nullable=False)
    HEADING_2: str = Field(nullable=True)
    SUM_AMOUNT: float = Field(nullable=True)
    FORMATTED_AMOUNT: float = Field(nullable=True)
    REPORT_DATE: datetime = Field(nullable=True)
    
class ManagerReport(ManagerReportBase, UUIDModel, table=True):
    __tablename__ = "manager_report"