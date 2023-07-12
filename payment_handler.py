from metaclass import ABCMeta, abstractmethod
from datetime import datetime


class IPaymentStrategy(metaclass=ABCMeta):
    """ Interface class for payment strategy objects """
    
    @abstractmethod
    def calculate_amount(self):
        pass

class HourlyPayment(IPaymentStrategy):
    
    def calculate_amount(self, parking_time):
        pass 

class DailyPayment(IPaymentStrategy):
    
    def calculate_amount(self, parking_time):
        pass 


class IPaymentMethod(metaclass=ABCMeta):
    # Implementing Template method with bridge

    def __init__(self, payment_strategy: IPaymentStrategy):
        self.payment_strategy = payment_strategy   # bridge

    def calculate_amount(self, ticket):     # template method
        parking_time = ticket.parking_time
        return self.payment_strategy.calculate_amount(parking_time)

    @abstractmethod
    def make_payment(self):
        pass 

class PayPal(IPaymentMethod):

    def make_payment():
        amount = self.calculate_amount(ticket)
        # custom payment logic

class CreditCardPayment(IPaymentMethod):

    def make_payment():
        amount = self.calculate_amount(ticket)
        # custom payment logic


class PaymentHandler:
    # Implementing facade method desing pattern

    payment_method_mapper = {
        "paypal": PayPalPayment(),
        "credit-card": CreditCardPayment()
    }

    payment_strategy_mapper = {
        "hourly": HourlyPayment(),
        "daily": DailyPayment()
    }

    def __init__(self, ticket, payment_strategy, payment_method):
        self.ticket = ticket
        self.payment_strategy = PaymentHandler.payment_strategy_mapper.get(payment_strategy, None)
        self.payment_method = PaymentHandler.payment_method_mapper.get(payment_method, None)
    
    #static methods can be inherited but cannot be overwritten
    @staticmethod
    def pay(ticket, payment_strategy, payment_method):
        self.payment_method(self.payment_strategy).make_payment(self.payment_strategy)