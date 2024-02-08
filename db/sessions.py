import csv
import os
from sqlmodel import SQLModel, create_engine, Session  
from dateutil.parser import parse
from core.config import settings  
from db.tables.base_class import SQLModel
from db.tables.journal import Journal  
from db.tables.manager_report import ManagerReport
from db.tables.trial_balance import TrialBalance
from datetime import datetime
  
engine = create_engine(  
    url=settings.sync_database_url,  
    echo=settings.db_echo_log,  
)  

def parse_none(dt):
    try:
        return parse(dt)
    except:
        return None


def prepare_journal(row):
    return Journal(**row)

def prepare_manager_report(row):
    return ManagerReport(**row)

def prepare_trial_balance(row):
    return TrialBalance(**row)
 
def create_multiple_entry(data):
    with Session(engine) as session:  
        session.add_all(data)  
        session.commit()  


def move_processed_files(processed_files):
    for file in processed_files:
        os.rename("Z:/" + file, "Z:/processed/" + file)

def get_date_from_file_name(file_name):
    date = file_name[0:8]
    try:
        return parse(date)
    except:
        return None
    

journals_name = "journal"
manager_reports_name = "manager_report"
trial_balances_name = "trial_balance"

def upload_to_tables():
    dir_files = os.listdir("Z:/")
    journals = []
    manager_reports = []
    trial_balances = []
    processed_files = []
    for file in dir_files:
        if file.endswith('.csv'):
            path_to_file = "Z:/" + file
            with open(file=path_to_file, encoding="utf-8", mode="r+") as csv_file:
                csvreader = csv.DictReader(f=csv_file, delimiter=';', quotechar='"')
                if file.lower().find(journals_name) != -1:
                    for row in csvreader:
                        if (row['TRX_NO'] == None):
                            continue
                        row['BUSINESS_DATE'] = parse_none(row['BUSINESS_DATE'])
                        row['BUSINESS_FORMAT_DATE'] = parse_none(row['BUSINESS_FORMAT_DATE'])
                        row['EXP_DATE'] = parse_none(row['EXP_DATE'])
                        
                        journals.append(prepare_journal(row))
                    processed_files.append(file)
                        
                if file.lower().find(manager_reports_name) != -1:
                    for row in csvreader:
                        if row["MASTER_VALUE_ORDER"] == None or row["MASTER_VALUE_ORDER"] == "" or not row["MASTER_VALUE_ORDER"].isdigit():
                            continue
                        
                        row["REPORT_DATE"] = get_date_from_file_name(file)
                        manager_reports.append(prepare_manager_report(row)) 
                               
                    processed_files.append(file)
                    
                if file.lower().find(trial_balances_name) != -1:
                    for row in csvreader:
                        if row["TRX_TYPE_SORT"] == None or row["TRX_TYPE_SORT"] == "" or not row["TRX_TYPE_SORT"].isdigit():
                            break
                        
                        row["TRX_DATE"] = parse_none(row["TRX_DATE"])
                        trial_balances.append(prepare_trial_balance(row))
                    processed_files.append(file)
                    
            if len(journals) > 0:
                create_multiple_entry(journals)
                
            if len(manager_reports) > 0:
                create_multiple_entry(manager_reports)
            
            if len(trial_balances) > 0:
                create_multiple_entry(trial_balances)
    
    move_processed_files(processed_files)
    
    
  
def create_tables():  
    SQLModel.metadata.drop_all(engine)  
    SQLModel.metadata.create_all(engine)