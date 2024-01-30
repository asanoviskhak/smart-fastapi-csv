from sqlmodel import Field, SQLModel

class ManagerReportBase(SQLModel):
    amount: int = Field(nullable=False)
    description: str = Field(nullable=False)
    
class ManagerReport(ManagerReportBase, table=True):
    __tablename__ = "manager_report"