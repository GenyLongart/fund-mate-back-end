from models import PaymentType 
from models.base import db
from sqlalchemy.orm import sessionmaker

class PaymentTypeService:

    def add_payment_type(self, paymentType):
        # Create a new user and save it to the database
        new_payment_type = PaymentType(**paymentType)

        db.session.add(new_payment_type)
        db.session.commit()

    def get_all_payment_types(self):
        Session = sessionmaker(bind=db.engine)
        session = Session()

        top_50_payment_types = session.query(PaymentType).limit(50).all()
        
        #close the session, we dont need anymore
        session.close()
        
        if len(top_50_payment_types) > 0:
            return top_50_payment_types
        else:
            raise Exception(f"Loans Query Error: There are no payment types in the database")
        