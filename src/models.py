from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'

    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Password = db.Column(db.String)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Username = db.Column(db.String(100), unique=True)
    Email = db.Column(db.String(100), unique=True)
    PhoneNumber = db.Column(db.String)
    MobileNumber = db.Column(db.String)
    Nationality = db.Column(db.String)
    #ProfilePicture = db.Column(db.Image)

    GoogleOAuth = db.relationship('GoogleOAuth', backref='user', uselist=False)
    Identity = db.relationship('Identity', backref='user', uselist=False)
    BankDetails = db.relationship('BankDetails', backref='user', uselist=False)
    Address = db.relationship('Address', backref='user', uselist=False)
    Lender = db.relationship('Lender', backref='user', uselist=False)
    Debtor = db.relationship('Debtor', backref='user', uselist=False)

class Admin(db.Model):
    __tablename__ = 'Admin'

    AdminID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Password = db.Column(db.String)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Username = db.Column(db.String(100), unique=True)
    Email = db.Column(db.String(100), unique=True)

class GoogleOAuth(db.Model):
    __tablename__ = 'GoogleOAuth'

    GoogleID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    GoogleOAuthID = db.Column(db.String, unique=True)
    GoogleName = db.Column(db.String)
    GoogleProfilePicture = db.Column(db.String)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))

class Identity(db.Model):
    __tablename__ = 'Identity'

    IdentityID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    IdentityDocumentLink = db.Column(db.String)
    IdentityFileName = db.Column(db.String(50))
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))

class BankDetails(db.Model):
    __tablename__ = 'BankDetails'

    BankID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    BankName = db.Column(db.String)
    BankCardNumber = db.Column(db.String(16))
    BankAccountNumber = db.Column(db.String(8))
    BankSortCode = db.Column(db.String(6))
    BankIssueDate = db.Column(db.DateTime)
    BankExpiryDate = db.Column(db.DateTime)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))

class Address(db.Model):
    __tablename__ = 'Address'

    AddressID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Street = db.Column(db.String)
    Apartment_Block = db.Column(db.String)
    Commune = db.Column(db.String)
    CityID = db.Column(db.Integer, db.ForeignKey('City.CityID'))
    RegionID = db.Column(db.Integer, db.ForeignKey('Region.RegionID'))
    Postcode = db.Column(db.String)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))

class City(db.Model):
    __tablename__ = 'City'

    CityID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CityName = db.Column(db.String)

class Region(db.Model):
    __tablename__ = 'Region'

    RegionID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    RegionName = db.Column(db.String)

class Lender(db.Model):
    __tablename__ = 'Lender'

    LenderID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))

class LenderToLoan(db.Model):
    __tablename__ = 'LenderToLoan'

    LenderToLoanID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    LenderID = db.Column(db.Integer, db.ForeignKey('Lender.LenderID'))
    LoanID = db.Column(db.Integer, db.ForeignKey('Loan.LoanID'))

class Debtor(db.Model):
    __tablename__ = 'Debtor'

    DebtorID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))

class Loan(db.Model):
    __tablename__ = 'Loan'

    LoanID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Amount = db.Column(db.Numeric)
    CreatedAt = db.Column(db.DateTime)
    UpdatedAt = db.Column(db.DateTime)
    Interest = db.Column(db.Integer)
    Negotiable = db.Column(db.Boolean)
    Description = db.Column(db.String(200))
    DueDate = db.Column(db.DateTime)

class LoanConditions(db.Model):
    __tablename__ = 'LoanConditions'

    LoanConditionID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    LoanID = db.Column(db.Integer, db.ForeignKey('Loan.LoanID'))
    LoanConditionDescription = db.Column(db.String(200))

class LoanOffer(db.Model):
    __tablename__ = 'LoanOffer'

    LoanOfferID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    LoanID = db.Column(db.Integer, db.ForeignKey('Loan.LoanID'))
    LenderID = db.Column(db.Integer, db.ForeignKey('Lender.LenderID'))
    DebtorID = db.Column(db.Integer, db.ForeignKey('Debtor.DebtorID'))
    OfferCreatedAt = db.Column(db.DateTime)
    OfferUpdatedAt = db.Column(db.DateTime)
    Interest = db.Column(db.Integer)
    DueDate = db.Column(db.DateTime)
    PaymentFrequency = db.Column(db.Integer, db.ForeignKey('PaymentFrequency.PaymentFrequencyID'))
    OfferStatus = db.Column(db.Integer, db.ForeignKey('OfferStatus.OfferStatusID'))

class PaymentFrequency(db.Model):
    __tablename__ = 'PaymentFrequency'

    PaymentFrequencyID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Frequency = db.Column(db.String, unique=True)

class OfferStatus(db.Model):
    __tablename__ = 'OfferStatus'

    OfferStatusID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Status = db.Column(db.String, unique=True)

class Transaction(db.Model):
    __tablename__ = 'Transaction'

    TransactionID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    LoanID = db.Column(db.Integer, db.ForeignKey('Loan.LoanID'))
    LenderID = db.Column(db.Integer, db.ForeignKey('Lender.LenderID'))
    DebtorID = db.Column(db.Integer, db.ForeignKey('Debtor.DebtorID'))
    TransactionCreatedAt = db.Column(db.DateTime)
    TransactionUpdatedAt = db.Column(db.DateTime)
    OriginalAmount = db.Column(db.Numeric)
    AmountDue = db.Column(db.Numeric)
    Interest = db.Column(db.Integer)
    DueDate = db.Column(db.DateTime)
    PaymentFrequency = db.Column(db.Integer, db.ForeignKey('PaymentFrequency.PaymentFrequencyID'))
    TransactionStatus = db.Column(db.Integer, db.ForeignKey('TransactionStatus.TransactionStatusID'))

class TransactionStatus(db.Model):
    __tablename__ = 'TransactionStatus'

    TransactionStatusID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Status = db.Column(db.String, unique=True)

class TransactionPayment(db.Model):
    __tablename__ = 'TransactionPayment'

    TransactionPaymentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TransactionID = db.Column(db.Integer, db.ForeignKey('Transaction.TransactionID'))
    AmountPaid = db.Column(db.Numeric)
    DatePaid = db.Column(db.DateTime)
    PaymentStatus = db.Column(db.Integer, db.ForeignKey('PaymentStatus.PaymentStatusID'))

class PaymentStatus(db.Model):
    __tablename__ = 'PaymentStatus'

    PaymentStatusID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Status = db.Column(db.String, unique=True)

class Contract(db.Model):
    __tablename__ = 'Contract'

    ContractID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TransactionID = db.Column(db.Integer, db.ForeignKey('Transaction.TransactionID'))
    ContractDocumentLink = db.Column(db.String)
    ContractFileName = db.Column(db.String(50))