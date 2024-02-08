from sqlmodel import Field, SQLModel
from datetime import datetime
from db.tables.base_class import UUIDModel


# CREATE TABLE "trial_balance" (
#   "TRX_TYPE_SORT" bigint,
#   "TRX_TYPE" text,
#   "TRX_TYPE_DESCRIPTION" text,
#   "IS_TB_TRX_TYPE_01" bigint,
#   "CS_TB_AMOUNT_TYPE" double precision,
#   "TRX_CODE_SORT" bigint,
#   "TRX_CODE" bigint,
#   "DESCRIPTION" text,
#   "TB_AMOUNT" double precision,
#   "TRX_DATE" text,
#   "NET_AMOUNT" double precision,
#   "GUEST_LED_DEBIT" text NULL,
#   "GUEST_LED_CREDIT" text NULL,
#   "AR_LED_DEBIT" bigint,
#   "AR_LED_CREDIT" text NULL,
#   "DEP_LED_DEBIT" double precision NULL,
#   "DEP_LED_CREDIT" text NULL,
#   "PACKAGE_LED_DEBIT" double precision NULL,
#   "PACKAGE_LED_CREDIT" text NULL,
#   "INH_DEBIT" bigint,
#   "INH_CREDIT" bigint,
#   "NON_REVENUE_AMT" double precision,
#   "TODAYS_ACCRUALS" double precision,
#   "DEPOSIT_AT_CHECKIN" text NULL,
#   "PACKAGE_LED_TAX" bigint NULL,
#   "DEP_TAX_LED_DEBIT" bigint,
#   "OWNER_LED_DEBIT" bigint,
#   "OWNER_LED_CREDIT" text NULL,
#   "DEP_LED_DEBIT_PL_CZ" bigint,
#   "CS_CURRENCY_COUNT" bigint,
#   "C_TRX_CODE" text,
#   "C_RESORT" text,
#   "C_TRX_DATE" text,
#   "C_TB_AMOUNT_NET" text,
#   "C_DISP_CURRENCY" text,
#   "C_GUEST_LED_CREDIT" text,
#   "C_GL_DISP_CURRENCY" text,
#   "C_AR_LED_CREDIT" text,
#   "C_AR_DISP_CURRENCY" text,
#   "C_DEP_LED_CREDIT" text,
#   "C_DL_DISP_CURRENCY" text,
#   "C_INH_LED_CREDIT" text,
#   "C_IH_DISP_CURRENCY" text,
#   "C_OWNER_LED_CREDIT" text,
#   "C_OWNER_DISP_CURRENCY" text
# );

class TrialBalanceBase(SQLModel):
    TRX_TYPE_SORT: int = Field(nullable=False)
    TRX_TYPE: str = Field(nullable=False)
    TRX_TYPE_DESCRIPTION: str = Field(nullable=True)
    IS_TB_TRX_TYPE_01: int = Field(nullable=True)
    CS_TB_AMOUNT_TYPE: float = Field(nullable=True)
    TRX_CODE_SORT: int = Field(nullable=True)
    TRX_CODE: int = Field(nullable=True)
    DESCRIPTION: str = Field(nullable=True)
    TB_AMOUNT: float = Field(nullable=False)
    TRX_DATE: datetime = Field(nullable=False)
    NET_AMOUNT: float = Field(nullable=True)
    GUEST_LED_DEBIT: float = Field(nullable=True)
    GUEST_LED_CREDIT: float = Field(nullable=True)
    AR_LED_DEBIT: float = Field(nullable=True)
    AR_LED_CREDIT: float = Field(nullable=True)
    DEP_LED_DEBIT: float = Field(nullable=True)
    DEP_LED_CREDIT: float = Field(nullable=True)
    PACKAGE_LED_DEBIT: float = Field(nullable=True)
    PACKAGE_LED_CREDIT: float = Field(nullable=True)
    INH_DEBIT: float = Field(nullable=True)
    INH_CREDIT: float = Field(nullable=True)
    NON_REVENUE_AMT: float = Field(nullable=True)
    TODAYS_ACCRUALS: float = Field(nullable=True)
    DEPOSIT_AT_CHECKIN: float = Field(nullable=True)
    PACKAGE_LED_TAX: float = Field(nullable=True)
    DEP_TAX_LED_DEBIT: float = Field(nullable=True)
    OWNER_LED_DEBIT: float = Field(nullable=True)
    OWNER_LED_CREDIT: float = Field(nullable=True)
    DEP_LED_DEBIT_PL_CZ: float = Field(nullable=True)
    CS_CURRENCY_COUNT: int = Field(nullable=True)
    C_TRX_CODE: str = Field(nullable=True)
    C_RESORT: str = Field(nullable=True)   
    C_TRX_DATE: str = Field(nullable=True)
    C_TB_AMOUNT_NET: str = Field(nullable=True)
    C_DISP_CURRENCY: str = Field(nullable=True)
    C_GUEST_LED_CREDIT: float = Field(nullable=True)
    C_GL_DISP_CURRENCY: str = Field(nullable=True)
    C_AR_LED_CREDIT: float = Field(nullable=True)
    C_AR_DISP_CURRENCY: str = Field(nullable=True)
    C_DEP_LED_CREDIT: float = Field(nullable=True)
    C_DL_DISP_CURRENCY: str = Field(nullable=True)
    C_INH_LED_CREDIT: float = Field(nullable=True)
    C_IH_DISP_CURRENCY: str = Field(nullable=True)
    C_OWNER_LED_CREDIT: float = Field(nullable=True)
    C_OWNER_DISP_CURRENCY: str = Field(nullable=True)

    
    
class TrialBalance(TrialBalanceBase, UUIDModel, table=True):
    __tablename__ = "trial_balance"