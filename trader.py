"""
Foram Stock Market Python test
"""
from Actions import StockActions, Action
from daily_report import DailyReport
from datetime import datetime as dt
import copy


class Trader:
    """
    A class for trader's actions.
    """
    def __init__(self):
        self._all_actions = []
        self._dividend_income = 0
        self._account = {}  # keep track of trader's account
        self._actions_by_date = {}  # classify actions by their date
        self.daily_report = {}

    def get_actions_by_date(self):
        """getter for action by date"""
        return self._actions_by_date

    def get_all_actions(self):
        """
        getter for the list of action
        """
        return self._all_actions

    def set_all_actions(self, all_actions):
        """setter for all_action"""
        self._all_actions.extend(all_actions)

    def get_divident_income(self):
        """
        getter for dividend_income
        """
        return self._dividend_income

    def get_account(self):
        """
        getter for trader's account
        """
        return self._account

    def update_account_action(self, action: Action):
        """update the account as trader make an action"""
        temp_dict = self._account
        if action.action == 'BUY':
            if action.ticker not in temp_dict:
                temp_dict[action.ticker] = [action.share, action.price]
            else:
                new_share = int(action.share) + int(temp_dict[action.ticker][0])
                total_price = int(action.share) * float(action.price) + \
                              int(temp_dict[action.ticker][0]) * float(temp_dict[action.ticker][1])
                new_price = total_price / new_share
                temp_dict[action.ticker] = [str(new_share), str(new_price)]
        else:
            if action.ticker not in temp_dict:
                raise Exception("invalid action")
            else:
                profit = str(round((float(action.price) - float(temp_dict[action.ticker][1])) * float(action.share), 2))
                action.profit = profit
                new_share = - int(action.share) + int(temp_dict[action.ticker][0])
                if new_share < 0:
                    raise Exception("invalid action")
                if new_share == 0:
                    del temp_dict[action.ticker]
                else:
                    temp_dict[action.ticker][0] = str(new_share)

    def update_account_stockaction(self, action: StockActions):
        """update account as stock make an action"""
        temp_dict = self._account
        if action.stock in self._account:
            if action.dividend == '':
                split = int(action.split)
                new_share = split * int(temp_dict[action.stock][0])
                new_price = round(float(temp_dict[action.stock][1])/split, 2)
                temp_dict[action.stock] = [str(new_share), str(new_price)]
                action.share = str(new_share)
            else:
                action.share = temp_dict[action.stock][0]
                dividend = round(float(action.dividend), 2)
                income = int(self._account[action.stock][0]) * dividend
                self._dividend_income += income

    def update_account(self, action):
        """update trader's account"""
        date = ''
        if isinstance(action, Action):
            self.update_account_action(action)
            date += action.date.split()[0]
        else:
            self.update_account_stockaction(action)
            date += action.date
        self.update_daily_report(date)

    def update_action_by_date(self):
        """update the action_by_date dictionary"""
        for action in self._all_actions:
            if isinstance(action, Action):
                date = action.date.split()[0]
                if date not in self._actions_by_date:
                    self._actions_by_date[date] = [action]
                else:
                    self._actions_by_date[date].append(action)
            else:
                if action.stock in self._account:
                    date = action.date
                    if date not in self._actions_by_date:
                        self._actions_by_date[date] = [action]
                    else:
                        self._actions_by_date[date].append(action)

    def update_daily_report(self, date: str):
        """update the daily_report by date"""
        report = DailyReport()
        report.report = copy.deepcopy(self._account)
        report.dividend_income = self._dividend_income
        self.daily_report[date] = report

    def __repr__(self):
        result = ''
        for date in self._actions_by_date:
            datetime_obj = dt.strptime(date, '%Y/%m/%d')
            result += "On {}, you have:\n".format(datetime_obj.strftime('%Y-%m-%d'))
            result += self.daily_report[date].__repr__()
            result += "  Transactions:\n"
            for action in self._actions_by_date[date]:
                result += action.__repr__()
        return result

