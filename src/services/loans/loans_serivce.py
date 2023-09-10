from models import LoanAdvertisement 
from models.base import db
import models.db_utils as db_utils
from sqlalchemy.orm import sessionmaker, joinedload

class LoansService:

    def add_new_loan_advertisment(self, loan_advertisment):

        new_loan_advertisment = LoanAdvertisement(**loan_advertisment)

        db.session.add(new_loan_advertisment)
        db.session.commit()

    def get_all_loans(self, session):
        #top_50_loan_advertisements = session.query(LoanAdvertisement).options(joinedload(LoanAdvertisement.lender), joinedload(LoanAdvertisement.paymentFrequency)).order_by(LoanAdvertisement.createdAt.desc()).limit(50).all()
        top_50_loan_advertisements = session.query(LoanAdvertisement).order_by(LoanAdvertisement.createdAt.desc()).limit(50).all()

        if len(top_50_loan_advertisements) > 0:
            return top_50_loan_advertisements
        else:
            raise Exception(f"Loans Query Error: There are no loan advertisments in the database")
        