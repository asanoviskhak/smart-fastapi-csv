from sqlmodel import Field, SQLModel
from datetime import datetime

# CREATE TABLE "journal" (
#   "IS_INTERNAL_YN" text,
#   "INTERNAL_DEBIT" bigint,
#   "INTERNAL_CREDIT" double precision,
#   "FIRST" text NULL,
#   "FIRST_DEBIT" bigint,
#   "FIRST_CREDIT" double precision,
#   "SECOND" text NULL,
#   "SECOND_DEBIT" bigint,
#   "SECOND_CREDIT" double precision,
#   "THIRD" text NULL,
#   "THIRD_DEBIT" bigint,
#   "THIRD_CREDIT" double precision,
#   "EXP_DATE" text NULL,
#   "RECEIPT_NO" text NULL,
#   "GUEST_FULL_NAME" text,
#   "TARGET_RESORT" text NULL,
#   "TRX_DESC" text,
#   "MARKET_CODE" text,
#   "BUSINESS_FORMAT_DATE" text,
#   "BUSINESS_TIME" text,
#   "BUSINESS_DATE" text,
#   "REFERENCE" text NULL,
#   "TRX_NO" bigint,
#   "CASHIER_DEBIT" double precision,
#   "CASHIER_CREDIT" double precision,
#   "ROOM" bigint,
#   "CREDIT_CARD_SUPPLEMENT" text NULL,
#   "CURRENCY1" text,
#   "TRX_CODE" bigint,
#   "CASHIER_ID" bigint,
#   "REMARK" text NULL,
#   "INSERT_USER" bigint,
#   "INSERT_DATE" text,
#   "CHEQUE_NUMBER" double precision NULL,
#   "ROOM_CLASS" text,
#   "CC_CODE" text NULL,
#   "CASHIER_NAME" text,
#   "USER_NAME" text,
#   "DEP_NET_TAX_AMT" bigint,
#   "DEPOSIT_DEBIT" bigint,
#   "CASH_ID_USER_NAME" text,
#   "PRINT_CASHIER_DEBIT" double precision,
#   "PRINT_CASHIER_CREDIT" double precision
# );

class JournalBase(SQLModel):
    IS_INTERNAL_YN: str = Field(nullable=False)
    INTERNAL_DEBIT: int = Field(nullable=True)
    INTERNAL_CREDIT: float = Field(nullable=True)
    FIRST: str = Field(nullable=True)
    FIRST_DEBIT: int = Field(nullable=True)
    FIRST_CREDIT: float = Field(nullable=True)
    SECOND: str = Field(nullable=True)
    SECOND_DEBIT: int = Field(nullable=True)
    SECOND_CREDIT: float = Field(nullable=True)
    THIRD: str = Field(nullable=True)
    THIRD_DEBIT: int = Field(nullable=True)
    THIRD_CREDIT: float = Field(nullable=True)
    EXP_DATE: str = Field(nullable=True)
    RECEIPT_NO: str = Field(nullable=True)
    GUEST_FULL_NAME: str = Field(nullable=True)
    TARGET_RESORT: str = Field(nullable=True)
    TRX_DESC: str = Field(nullable=False)
    MARKET_CODE: str = Field(nullable=False)
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
    ROOM: int = Field(nullable=False)
    CREDIT_CARD_SUPPLEMENT: str = Field(nullable=True)
    CURRENCY1: str = Field(nullable=False)
    TRX_CODE: int = Field(nullable=False)
    CASHIER_ID: int = Field(nullable=False)
    REMARK: str = Field(nullable=True)
    INSERT_USER: int = Field(nullable=False)
    INSERT_DATE: datetime = Field(nullable=True)
    CHEQUE_NUMBER: float = Field(nullable=True)
    ROOM_CLASS: str = Field(nullable=False)
    CC_CODE: str = Field(nullable=True)
    CASHIER_NAME: str = Field(nullable=False)
    USER_NAME: str = Field(nullable=False)
    DEP_NET_TAX_AMT: int = Field(nullable=False)
    DEPOSIT_DEBIT: int = Field(nullable=False)
    CASH_ID_USER_NAME: str = Field(nullable=False)
    PRINT_CASHIER_DEBIT: float = Field(nullable=False)
    PRINT_CASHIER_CREDIT: float = Field(nullable=False)
   
    
class Journal(JournalBase, table=True):
    __tablename__ = "journal"