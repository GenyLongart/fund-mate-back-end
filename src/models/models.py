# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

# # class User(db.Model):
# #     __tablename__ = 'User'

# #     UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
# #     Username = db.Column(db.String(100), nullable=False, unique=True)
# #     Password = db.Column(db.String(120), nullable=False)
# #     FirstName = db.Column(db.String(50), nullable=False )
# #     LastName = db.Column(db.String(50), nullable=False)
# #     Email = db.Column(db.String(100), nullable=False, unique=True)
# #     PhoneNumber = db.Column(db.String(20), nullable=False)
# #     #MobileNumber = db.Column(db.String(20), nullable=False)
# #     #Nationality = db.Column(db.String(50), nullable=False)
# #     #ProfilePicture = db.Column(db.Image)

# #     GoogleOAuth = db.relationship('GoogleOAuth', backref='user', uselist=False, cascade="all, delete-orphan")
# #     Identity = db.relationship('Identity', backref='user', uselist=False, cascade="all, delete-orphan")
# #     BankDetails = db.relationship('BankDetails', backref='user', uselist=False, cascade="all, delete-orphan")
# #     #Address = db.relationship('Address', backref='user', uselist=False, cascade="all, delete-orphan")
# #     Lender = db.relationship('Lender', backref='user', uselist=False, cascade="all, delete-orphan")
# #     Debtor = db.relationship('Debtor', backref='user', uselist=False, cascade="all, delete-orphan")

# #     def save(self):
# #         db.session.add(self)
# #         db.session.commit()
        
# #     def update(self):
# #         db.session.commit()
    
# #     def delete(self):
# #         db.session.delete(self)
# #         db.session.commit()

# class Admin(db.Model):
#     __tablename__ = 'Admin'

#     AdminID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     Password = db.Column(db.String(120), nullable=False)
#     FirstName = db.Column(db.String(50), nullable=False )
#     LastName = db.Column(db.String(50), nullable=False)
#     Username = db.Column(db.String(100), nullable=False, unique=True)
#     Email = db.Column(db.String(100), nullable=False, unique=True)

# class GoogleOAuth(db.Model):
#     __tablename__ = 'GoogleOAuth'

#     GoogleID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     GoogleOAuthID = db.Column(db.String, nullable=False, unique=True)
#     GoogleName = db.Column(db.String, nullable=False)
#     GoogleProfilePicture = db.Column(db.String)
#     UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))

# class Identity(db.Model):
#     __tablename__ = 'Identity'

#     IdentityID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     IdentityNumber = db.Column(db.String(20), nullable=False)
#     IdentityDocumentLink = db.Column(db.String, nullable=False)
#     IdentityFileName = db.Column(db.String(50), nullable=False)
#     IdentityType = db.Column(db.String(15), nullable=False)
#     UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))

# class BankDetails(db.Model):
#     __tablename__ = 'BankDetails'

#     BankID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     BankName = db.Column(db.String, nullable=False)
#     BankCardNumber = db.Column(db.String(16), nullable=False)
#     BankAccountNumber = db.Column(db.String(8), nullable=False)
#     BankSortCode = db.Column(db.String(6), nullable=False)
#     BankIssueDate = db.Column(db.DateTime, nullable=False)
#     BankExpiryDate = db.Column(db.DateTime, nullable=False)
#     UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))

# # class Address(db.Model):
# #     __tablename__ = 'Address'

# #     AddressID = db.Column(db.Integer, primary_key=True, autoincrement=True)
# #     Street = db.Column(db.String, nullable=False)
# #     Apartment_Block = db.Column(db.String)
# #     Commune = db.Column(db.String, nullable=False)
# #     CityID = db.Column(db.Integer, db.ForeignKey('City.CityID'), nullable=False)
# #     RegionID = db.Column(db.Integer, db.ForeignKey('Region.RegionID'), nullable=False)
# #     Postcode = db.Column(db.String, nullable=False)
# #     UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'), nullable=False)

# class City(db.Model):
#     __tablename__ = 'City'

#     CityID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     CityName = db.Column(db.String, nullable=False)

# class Region(db.Model):
#     __tablename__ = 'Region'

#     RegionID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     RegionName = db.Column(db.String, nullable=False)

# class Lender(db.Model):
#     __tablename__ = 'Lender'

#     LenderID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'), nullable=False)

# class LenderToLoan(db.Model):
#     __tablename__ = 'LenderToLoan'

#     LenderToLoanID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     LenderID = db.Column(db.Integer, db.ForeignKey('Lender.LenderID'), nullable=False)
#     LoanID = db.Column(db.Integer, db.ForeignKey('Loan.LoanID'), nullable=False)

# class Debtor(db.Model):
#     __tablename__ = 'Debtor'

#     DebtorID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'), nullable=False)

# class Loan(db.Model):
#     __tablename__ = 'Loan'

#     LoanID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     Amount = db.Column(db.Numeric, nullable=False)
#     CreatedAt = db.Column(db.DateTime, nullable=False)
#     UpdatedAt = db.Column(db.DateTime, nullable=False)
#     Interest = db.Column(db.Integer, nullable=False)
#     Negotiable = db.Column(db.Boolean, nullable=False)
#     Description = db.Column(db.String(200))
#     DueDate = db.Column(db.DateTime, nullable=False)

# class LoanConditions(db.Model):
#     __tablename__ = 'LoanConditions'

#     LoanConditionID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     LoanID = db.Column(db.Integer, db.ForeignKey('Loan.LoanID'), nullable=False)
#     LoanConditionDescription = db.Column(db.String(200), nullable=False)

# class LoanOffer(db.Model):
#     __tablename__ = 'LoanOffer'

#     LoanOfferID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     LoanID = db.Column(db.Integer, db.ForeignKey('Loan.LoanID'), nullable=False)
#     LenderID = db.Column(db.Integer, db.ForeignKey('Lender.LenderID'), nullable=False)
#     DebtorID = db.Column(db.Integer, db.ForeignKey('Debtor.DebtorID'), nullable=False)
#     OfferCreatedAt = db.Column(db.DateTime, nullable=False)
#     OfferUpdatedAt = db.Column(db.DateTime, nullable=False)
#     Interest = db.Column(db.Integer, nullable=False)
#     DueDate = db.Column(db.DateTime, nullable=False)
#     PaymentFrequency = db.Column(db.Integer, db.ForeignKey('PaymentFrequency.PaymentFrequencyID'), nullable=False)
#     OfferStatus = db.Column(db.Integer, db.ForeignKey('OfferStatus.OfferStatusID'), nullable=False)

# class PaymentFrequency(db.Model):
#     __tablename__ = 'PaymentFrequency'

#     PaymentFrequencyID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     Frequency = db.Column(db.String, unique=True, nullable=False)

# class OfferStatus(db.Model):
#     __tablename__ = 'OfferStatus'

#     OfferStatusID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     Status = db.Column(db.String, unique=True, nullable=False)

# class Transaction(db.Model):
#     __tablename__ = 'Transaction'

#     TransactionID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     LoanID = db.Column(db.Integer, db.ForeignKey('Loan.LoanID'), nullable=False)
#     LenderID = db.Column(db.Integer, db.ForeignKey('Lender.LenderID'), nullable=False)
#     DebtorID = db.Column(db.Integer, db.ForeignKey('Debtor.DebtorID'), nullable=False)
#     TransactionCreatedAt = db.Column(db.DateTime, nullable=False)
#     TransactionUpdatedAt = db.Column(db.DateTime, nullable=False)
#     OriginalAmount = db.Column(db.Numeric, nullable=False)
#     AmountDue = db.Column(db.Numeric, nullable=False)
#     Interest = db.Column(db.Integer, nullable=False)
#     DueDate = db.Column(db.DateTime, nullable=False)
#     PaymentFrequency = db.Column(db.Integer, db.ForeignKey('PaymentFrequency.PaymentFrequencyID'), nullable=False)
#     TransactionStatus = db.Column(db.Integer, db.ForeignKey('TransactionStatus.TransactionStatusID'), nullable=False)

# class TransactionStatus(db.Model):
#     __tablename__ = 'TransactionStatus'

#     TransactionStatusID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     Status = db.Column(db.String, unique=True, nullable=False)

# class TransactionPayment(db.Model):
#     __tablename__ = 'TransactionPayment'

#     TransactionPaymentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     TransactionID = db.Column(db.Integer, db.ForeignKey('Transaction.TransactionID'), nullable=False)
#     AmountPaid = db.Column(db.Numeric, nullable=False)
#     DatePaid = db.Column(db.DateTime, nullable=False)
#     PaymentStatus = db.Column(db.Integer, db.ForeignKey('PaymentStatus.PaymentStatusID'), nullable=False)

# class PaymentStatus(db.Model):
#     __tablename__ = 'PaymentStatus'

#     PaymentStatusID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     Status = db.Column(db.String, unique=True, nullable=False)

# class Contract(db.Model):
#     __tablename__ = 'Contract'

#     ContractID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     TransactionID = db.Column(db.Integer, db.ForeignKey('Transaction.TransactionID'), nullable=False)
#     ContractDocumentLink = db.Column(db.String, nullable=False)
#     ContractFileName = db.Column(db.String(50), nullable=False)