from sqlmodel import Field, SQLModel

class TrialBalanceBase(SQLModel, ):
    amount: int = Field(nullable=False)
    description: str = Field(nullable=False)
    
class TrialBalance(TrialBalanceBase, table=True):
    __tablename__ = "trial_balance"