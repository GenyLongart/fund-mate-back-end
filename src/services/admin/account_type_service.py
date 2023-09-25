from models import AccountType 
from models.base import db
from sqlalchemy.orm import sessionmaker

class AccountTypeService:

    def add_account_type(self, accountType):
        new_account_type = AccountType(**accountType)

        db.session.add(new_account_type)
        db.session.commit()

    def get_all_account_types(self):
        Session = sessionmaker(bind=db.engine)
        session = Session()

        top_50_account_types = session.query(AccountType).limit(50).all()
        
        #close the session, we dont need anymore
        session.close()
        
        if len(top_50_account_types) > 0:
            return top_50_account_types
        else:
            raise Exception(f"Admin Query Error: There are no account types in the database")
        
    def delete_account_type(self, account_type_id):
        account_type = AccountType.query.filter_by(accountTypeID=account_type_id).first()

        if not account_type:
            return False
        
        db.session.delete(account_type)
        db.session.commit()

        return True
        