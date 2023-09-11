from models import Bank 
from models.base import db
from sqlalchemy.orm import sessionmaker

class BankService:

    def add_bank(self, bank):
        new_bank = Bank(**bank)

        db.session.add(new_bank)
        db.session.commit()

    def get_all_banks(self):
        Session = sessionmaker(bind=db.engine)
        session = Session()

        top_50_banks = session.query(Bank).limit(50).all()
        
        #close the session, we dont need anymore
        session.close()
        
        if len(top_50_banks) > 0:
            return top_50_banks
        else:
            raise Exception(f"Admin Query Error: There are no banks in the database")
        