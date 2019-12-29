from Actions import two_decimal_str


class DailyReport:
    """
    class for daily report
    """
    def __init__(self):
        self.report = {}
        self.dividend_income = 0

    def __repr__(self):

        s = ''
        for stock in self.report:
            price = two_decimal_str(self.report[stock][1])
            s += '\t- {} shares of {} at ${} per share\n'.format(self.report[stock][0], stock, price)
        if self.dividend_income == 0:
            s += "\t- ${} of dividend income\n".format(str(self.dividend_income))
        else:
            s += "\t- ${} of dividend income\n".format(two_decimal_str(str(self.dividend_income)))
        return s


