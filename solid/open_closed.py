from abc import ABC, abstractmethod


class Order:
    items: list[str] = []
    quantities: list[int] = []
    prices: list[float] = []
    status = "open"

    def add_items(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0

        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]

        return total


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass


class DebitPayment(PaymentProcessor):

    def pay(self, order, security_code):

        print('Processing debit payment type...')
        print(f'Verifying security code: {security_code}')
        order.status = "paid"


class CreditPayment(PaymentProcessor):

    def pay(self, order, security_code):
        print('Processing credit payment type...')
        print(f'Verifying security code: {security_code}')
        order.status = "paid"


class PaypalPayment(PaymentProcessor):

    def pay(self, order, security_code):
        print('Processing paypal payment type...')
        print(f'Verifying security code: {security_code}')
        order.status = "paid"


order = Order()

order.add_items("Keyboard", 1, 50)
order.add_items("SSD", 1, 150)
order.add_items("USB cable", 2, 5)

print(order.total_price())

processor = PaypalPayment()


processor.pay(order, "0372846")
