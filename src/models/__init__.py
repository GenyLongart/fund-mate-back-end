from .contract import Contract
from .debtor.debtor import Debtor
from .lender.lender import Lender
from .loan.loanAdvertisement import LoanAdvertisement
from .loan.loanConditions import LoanConditions
from .loan.loanOffer import LoanOffer
from .payment.paymentStatus import PaymentStatus
from .payment.paymentFrequency import PaymentFrequency
from .transaction.transaction import Transaction
from .transaction.transactionPayment import TransactionPayment
from .transaction.transactionStatus import TransactionStatus
from .user.user import User
from .user.googleOAuth import GoogleOAuth
from .user.identity import Identity
from .user.bankDetails import BankDetails
from .user.dicom import Dicom

# list of all models
all_models = [Contract, User, GoogleOAuth, Identity, BankDetails, Lender, Debtor, Dicom, LoanAdvertisement, LoanConditions, LoanOffer, PaymentStatus, PaymentFrequency, Transaction, TransactionPayment, TransactionStatus]