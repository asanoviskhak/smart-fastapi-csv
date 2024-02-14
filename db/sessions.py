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

months = {
        "JAN": 1,
        "FEB": 2,
        "MAR": 3,
        "APR": 4,
        "MAY": 5,
        "JUN": 6,
        "JUL": 7,
        "AUG": 8,
        "SEP": 9,
        "OCT": 10,
        "NOV": 11,
        "DEC": 12
    }
    

def parse_none(dt, default=None, words=None):
    try:
        if default:
            day = dt[0:2]
            month = dt[3:5]
            year = "20" + dt[6:8]
            return datetime(int(year), int(month), int(day))
        
        if words:
            splitted = dt.split("-")
            day = splitted[0]
            month = months[splitted[1]]
            year = "20" + splitted[2]
            return datetime(int(year), int(month), int(day))
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
    try:
        char_at_10 = file_name[9]
        if char_at_10.isdigit():
            date = file_name[0:10]
            day = date[0:2]
            month = date[3:5]
            year =  date[6:10]
            return datetime(int(year), int(month), int(day))
        date = file_name[0:8]
        day = date[0:2]
        month = date[3:5]
        year = "20" + date[6:8]
        return datetime(int(year), int(month), int(day))
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
                        row['BUSINESS_DATE'] = parse_none(row['BUSINESS_DATE'], False, True)
                        row['BUSINESS_FORMAT_DATE'] = parse_none(row['BUSINESS_FORMAT_DATE'], True)
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
                        
                        row["TRX_DATE"] = parse_none(row["TRX_DATE"], False, True)
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