from abc import ABC, abstractmethod


class Bank(ABC):
    def branch(self, Naira):
        print("Fees submitted : ", Naira)

    @abstractmethod
    def Bank(Naira):


class private(Bank):
    def Bank(naira):
        print("Total Naira Value here: ", Naira)


class public(bank):
    def Bank(Naira):
        print("Total Naira Value here:", Naira)


protected.Bank(5000)
public.Bank(2000)

a = public()
# a.branch(3500)