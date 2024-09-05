from sqlalchemy.orm import Session
from db_setup import get_session
from models import XdrData

def get_all_records(db: Session):
    "Retrieve all records from the xdr_data table"
    return db.query(XdrData).all()

def main():
    "Main function to demonstrate querying the database"
    session = get_session()
    try:
        records = get_all_records(session)
        for record in records:
            print(record)
    finally:
        session.close()

if __name__ == "__main__":
    main()
