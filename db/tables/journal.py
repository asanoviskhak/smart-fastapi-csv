from sqlmodel import Field, SQLModel
from datetime import datetime

class JournalBase(SQLModel):
    IS_INTERNAL_YN: str = Field(nullable=True)
    INTERNAL_DEBIT: float = Field(nullable=True)
    INTERNAL_CREDIT: float = Field(nullable=True)
    FIRST: float = Field(nullable=True)
    FIRST_DEBIT: float = Field(nullable=True)
    FIRST_CREDIT: float = Field(nullable=True)
    SECOND: float = Field(nullable=True)
    SECOND_DEBIT: float = Field(nullable=True)
    SECOND_CREDIT: float = Field(nullable=True)
    THIRD: float = Field(nullable=True)
    THIRD_DEBIT: float = Field(nullable=True)
    THIRD_CREDIT: float = Field(nullable=True)
    EXP_DATE: str = Field(nullable=True)
    RECEIPT_NO: str = Field(nullable=True)
    GUEST_FULL_NAME: str = Field(nullable=True)
    TARGET_RESORT: str = Field(nullable=True)
    TRX_DESC: str = Field(nullable=True)
    MARKET_CODE: str = Field(nullable=True)
    BUSINESS_FORMAT_DATE: datetime = Field(nullable=False)
    BUSINESS_TIME: str = Field(nullable=True)
    BUSINESS_DATE: str = Field(nullable=True)
    REFERENCE: str = Field(nullable=True)
    TRX_NO: int = Field(
        primary_key=True,
        index=True,
        nullable=False,
    )
    CASHIER_DEBIT: float = Field(nullable=False)
    CASHIER_CREDIT: float = Field(nullable=False)
    ROOM: int = Field(nullable=True)
    CREDIT_CARD_SUPPLEMENT: str = Field(nullable=True)
    CURRENCY1: str = Field(nullable=True)
    TRX_CODE: int = Field(nullable=False)
    CASHIER_ID: int = Field(nullable=True)
    REMARK: str = Field(nullable=True)
    INSERT_USER: int = Field(nullable=False)
    INSERT_DATE: datetime = Field(nullable=True)
    CHEQUE_NUMBER: float = Field(nullable=True)
    ROOM_CLASS: str = Field(nullable=False)
    CC_CODE: str = Field(nullable=True)
    CASHIER_NAME: str = Field(nullable=True)
    USER_NAME: str = Field(nullable=False)
    DEP_NET_TAX_AMT: float = Field(nullable=False)
    DEPOSIT_DEBIT: float = Field(nullable=False)
    CASH_ID_USER_NAME: str = Field(nullable=False)
    PRINT_CASHIER_DEBIT: float = Field(nullable=False)
    PRINT_CASHIER_CREDIT: float = Field(nullable=False)
   
    
class Journal(JournalBase, table=True):
    __tablename__ = "journal"