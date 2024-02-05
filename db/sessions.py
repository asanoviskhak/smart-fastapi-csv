import csv
import pathlib
import os
from sqlmodel import SQLModel, create_engine, Session  
from dateutil.parser import parse
from core.config import settings  
from db.tables.base_class import SQLModel
from db.tables.journal import Journal  
  
  
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
 
def create_journal(data):
    with Session(engine) as session:  
        session.add_all(data)  
        session.commit()  
    
  

path_to_file = "/mnt/z"
print(path_to_file)
print(os.listdir(path_to_file))



# read from csv file and create a journal entry
def upload_to_tables():
    print('uploading to tables')
    journals = []
    with open(file=path_to_file, mode="r+") as csv_file:
        csvreader = csv.DictReader(f=csv_file, delimiter=';', quotechar='"')
        for row in csvreader:
            row['BUSINESS_DATE'] = parse_none(row['BUSINESS_DATE'])
            row['BUSINESS_TIME'] = parse_none(row['BUSINESS_TIME'])
            row['BUSINESS_FORMAT_DATE'] = parse_none(row['BUSINESS_FORMAT_DATE'])
            row['EXP_DATE'] = parse_none(row['EXP_DATE'])
            journals.append(prepare_journal(row))
    create_journal(journals)

    
  
def create_tables():  
    SQLModel.metadata.drop_all(engine)  
    SQLModel.metadata.create_all(engine)