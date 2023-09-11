from models import BankDetails
from models.base import db

class BankService:
    def edit_user_details(self, user, bank_details_data):
        # Create new bank details from bank data
        bank_details = BankDetails(**bank_details_data)
        user.bankDetails = bank_details

        db.session.commit()
        return user