from abc import ABC, abstractmethod


class Bill(ABC):
    def final_bill(self, pay):
        print('Purchase of the product: ', pay)

    @abstractmethod
    def Invoice(self, pay):
        pass


class Paycheque(Bill):
    def Invoice(self, pay):
        print('paycheque of: ', pay)


class CardPayment(Bill):
    def Invoice(self, pay):
        print('pay through card of: ', pay)


aa = Paycheque()
aa.Invoice(6500)
aa.final_bill(6500)
print(isinstance(aa, Invoice))
aa = CardPayment()
aa.Invoice(2600)
aa.final_bill(2600)
print(isinstance(aa, Invoice))