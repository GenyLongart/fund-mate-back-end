from models import PaymentFrequency 
from models.base import db
from sqlalchemy.orm import sessionmaker

class PaymentFrequencyTypeService:

    def add_payment_frequency_type(self, paymentType):
        new_payment_type = PaymentFrequency(**paymentType)

        db.session.add(new_payment_type)
        db.session.commit()

    def get_all_payment_frequency_types(self):
        Session = sessionmaker(bind=db.engine)
        session = Session()

        top_50_payment_types = session.query(PaymentFrequency).limit(50).all()
        
        #close the session, we dont need anymore
        session.close()
        
        if len(top_50_payment_types) > 0:
            return top_50_payment_types
        else:
            raise Exception(f"Loans Query Error: There are no payment frequency types in the database")
        