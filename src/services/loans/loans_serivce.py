from models import LoanAdvertisement 
from models.base import db
from sqlalchemy.orm import sessionmaker

class LoansService:
    def get_all_loans(self):
        Session = sessionmaker(bind=db.engine)
        session = Session()

        top_50_loan_advertisements = session.query(LoanAdvertisement).\
            order_by(LoanAdvertisement.createdAt.desc()).\
                limit(50)
        
        #close the session, we dont need anymore
        session.close()
                
        if top_50_loan_advertisements.count() > 0:
            return top_50_loan_advertisements
        else:
            raise Exception(f"Loans Query Error: There are no loan advertisments in the database")
        