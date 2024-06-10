from abc import ABC, abstractmethod


# Abstract Class
class product(ABC):

    # Normal Method
    def item_list(self, rate):
        print("amount submitted : ", rate)

    # Abstract Method
    @abstractmethod
    def product(self, rate):
        
