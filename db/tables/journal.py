from sqlmodel import Field, SQLModel

class JournalBase(SQLModel):
    amount: int = Field(nullable=False)
    description: str = Field(nullable=False)
    
class Journal(JournalBase, table=True):
    __tablename__ = "journal"