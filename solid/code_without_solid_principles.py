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

    def pay(self, payment_type, security_code):

        if payment_type == "debit":
            print('Processing debit payment type...')
            print(f'Verifying security code: {security_code}')
            self.status = "paid"
        elif payment_type == "credit":
            print('Processing credit payment type...')
            print(f'Verifying security code: {security_code}')
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


order = Order()

order.add_items("Keyboard", 1, 50)
order.add_items("SSD", 1, 150)
order.add_items("USB cable", 2, 5)

print(order.total_price())
order.pay("debit", "0372846")
