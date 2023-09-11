from .activeLoanTransaction.activeLoan import ActiveLoan
from .activeLoanTransaction.transactionPayment import TransactionPayment
from .activeLoanTransaction.transactionStatus import TransactionStatus
from .bankAccount.accountType import AccountType
from .bankAccount.bank import Bank
from .contract import Contract
from .debtor.debtor import Debtor
from .lender.lender import Lender
from .loan.loanAdvertisement import LoanAdvertisement
from .loan.loanConditions import LoanConditions
from .loan.loanOffer import LoanOffer
from .loan import OfferStatus
from .payment.paymentStatus import PaymentStatus
from .payment.paymentFrequency import PaymentFrequency
from .user.user import User
from .user.googleOAuth import GoogleOAuth
from .user.identity import Identity
from .user.bankDetails import BankDetails
from .user.dicom import Dicom

# list of all models
all_models = [AccountType, Bank, Contract, User, GoogleOAuth, Identity, BankDetails, Lender, Debtor, Dicom, LoanAdvertisement, LoanConditions, LoanOffer, OfferStatus, PaymentStatus, PaymentFrequency, ActiveLoan, TransactionPayment, TransactionStatus]