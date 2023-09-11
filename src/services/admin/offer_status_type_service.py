from models import OfferStatus 
from models.base import db
from sqlalchemy.orm import sessionmaker

class OfferStatusTypeService:

    def add_offer_status_type(self, offerType):
        new_offer_type = OfferStatus(**offerType)

        db.session.add(new_offer_type)
        db.session.commit()

    def get_all_offer_status_types(self):
        Session = sessionmaker(bind=db.engine)
        session = Session()

        top_50_offer_types = session.query(OfferStatus).limit(50).all()
        
        #close the session, we dont need anymore
        session.close()
        
        if len(top_50_offer_types) > 0:
            return top_50_offer_types
        else:
            raise Exception(f"Loans Query Error: There are no offer status types in the database")
        