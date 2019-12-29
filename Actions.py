"""
Foram Stock Market Python test
"""


class Actions:
    """Container for both kinds of actions"""
    pass


class StockActions(Actions):
    """
    A class for stock_actions
    """
    def __init__(self, date: str, dividend: str, split: str, stock: str):
        self.date = date
        self.dividend = dividend
        self.split = split
        self.stock = stock
        self.share = 0

    def __repr__(self):
        if self.split == '':
            return "\t- {} paid out ${} dividend per share, and you have {} shares\n".format(
                self.stock,  self.dividend, self.share)
        else:
            return "\t- {} split {} to 1, and you have {} shares\n".format(
                self.stock, self.split, self.share)


class Action(Actions):
    """
    A class for trading action
    """
    def __init__(self, date: str, action: str, price: str, ticker: str, share: str):
        """
        A initializer for an action of trader
        """
        self.date = date
        self.action = action
        self.price = price
        self.ticker = ticker
        self.share = share
        self.profit = 0

    def __repr__(self):
        price = two_decimal_str(self.price)
        profit = two_decimal_str(str(self.profit))
        if self.action == 'BUY':
            return "\t- You bought {} shares of {} at a price of ${} per share\n".format(
                self.share, self.ticker, price)
        else:
            return "\t- You sold {} shares of {} at a price of ${} per share" \
                   " for a profit of ${}\n".format(self.share, self.ticker, price, profit)


def two_decimal_str(s: str):
    """helper function to transform data into 2 decimal float"""
    return str(format(float(s), '.2f'))
