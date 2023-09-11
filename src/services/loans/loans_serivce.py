from models import LoanAdvertisement , LoanOffer
from models.base import db
import models.db_utils as db_utils
from sqlalchemy.orm import sessionmaker, joinedload

class LoansService:

    def add_new_loan_advertisment(self, loan_advertisment):

        new_loan_advertisment = LoanAdvertisement(**loan_advertisment)

        db.session.add(new_loan_advertisment)
        db.session.commit()
    
    def add_new_loan_offer(self, loan_offer):

        new_loan_offer = LoanOffer(**loan_offer)

        db.session.add(new_loan_offer)
        db.session.commit()

    def get_loan_advertisement(self, loan_advertisement_id):
        return LoanAdvertisement.query.filter_by(loanAdvertisementID=loan_advertisement_id).first()
    
    def get_loan_offer(self, loan_offer_id):
        return LoanOffer.query.filter_by(loanOfferID=loan_offer_id).first()

    def get_all_loans_advertisements(self, session):
        #top_50_loan_advertisements = session.query(LoanAdvertisement).options(joinedload(LoanAdvertisement.lender), joinedload(LoanAdvertisement.paymentFrequency)).order_by(LoanAdvertisement.createdAt.desc()).limit(50).all()
        top_50_loan_advertisements = session.query(LoanAdvertisement).order_by(LoanAdvertisement.createdAt.desc()).limit(50).all()

        if len(top_50_loan_advertisements) > 0:
            return top_50_loan_advertisements
        else:
            raise Exception(f"Loans Query Error: There are no loan advertisments in the database")
        
    def get_filtered_loan_advertisements(self, session, amount):
        if amount is not None:
            filtered_loans = session.query(LoanAdvertisement).filter(LoanAdvertisement.amount == amount).order_by(LoanAdvertisement.createdAt.desc()).all()
            if len(filtered_loans) > 0:
                return filtered_loans
            else:
                raise Exception(f"Loans Query Error: There are no loan advertisments in the database for that filtered query")
        else:
            return self.get_all_loans_advertisements(session)
        
    def get_loan_advertisements_by_lender(self, session, _lenderID):
        filtered_loan_advertisements = session.query(LoanAdvertisement).filter(LoanAdvertisement.lenderID == _lenderID).order_by(LoanAdvertisement.createdAt.desc()).all()
        if len(filtered_loan_advertisements) > 0:
            return filtered_loan_advertisements
        else:
            raise Exception(f"Loans Query Error: There are no loan advertisements in the database for that particular debtor")

    def get_loan_offers_by_debtor(self, session, _debtorID):
        filtered_loan_offers = session.query(LoanOffer).filter(LoanOffer.debtorID == _debtorID).order_by(LoanOffer.createdAt.desc()).all()
        if len(filtered_loan_offers) > 0:
            return filtered_loan_offers
        else:
            raise Exception(f"Loans Query Error: There are no loan offers in the database for that particular debtor")