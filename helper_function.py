from Actions import StockActions, Action
from datetime import datetime as dt
from trader import Trader

actions = [{'date': '1992/07/14 11:12:30', 'action': 'BUY', 'price': '12.3', 'ticker': 'AAPL', 'shares': '500'}, {'date': '1992/09/13 11:15:20', 'action': 'SELL', 'price': '15.3', 'ticker': 'AAPL', 'shares': '100'}, {'date': '1992/10/14 15:14:20', 'action': 'BUY', 'price': '20', 'ticker': 'MSFT', 'shares': '300'}, {'date': '1992/10/17 16:14:30', 'action': 'SELL', 'price': '20.2', 'ticker': 'MSFT', 'shares': '200'}, {'date': '1992/10/19 15:14:20', 'action': 'BUY', 'price': '21', 'ticker': 'MSFT', 'shares': '500'}, {'date': '1992/10/23 16:14:30', 'action': 'SELL', 'price': '18.2', 'ticker': 'MSFT', 'shares': '600'}, {'date': '1992/10/25 10:15:20', 'action': 'SELL', 'price': '20.3', 'ticker': 'AAPL', 'shares': '300'}, {'date': '1992/10/25 16:12:10', 'action': 'BUY', 'price': '18.3', 'ticker': 'MSFT', 'shares': '500'}]
stock_actions = [{'date': '1992/08/14', 'dividend': '0.10', 'split': '', 'stock': 'AAPL'},
                 {'date': '1992/09/01', 'dividend': '', 'split': '3', 'stock': 'AAPL'},
                 {'date': '1992/10/15', 'dividend': '0.20', 'split': '', 'stock': 'MSFT'},
                 {'date': '1992/10/16', 'dividend': '0.20', 'split': '', 'stock': 'ABC'}]


def helper_load_actions(actions_list: list):
    """
    A helper function to save each action as an instance object of class Action and load all trader's action to a list
    """
    result = []
    for action in actions_list:
        temp = Action(action['date'], action['action'], action['price'], action['ticker'], action['shares'])
        result.append(temp)
    return result


def helper_load_stock_actions(stock_actions_list: list):
    """
    A helper function to save all stock action as an instance of StockAction and load all stock action to a list
    """
    result = []
    for action in stock_actions_list:
        temp = StockActions(action['date'], action['dividend'], action['split'], action['stock'])
        result.append(temp)
    return result


def helper_strdate_to_date_action(date: str):
    """a helper that change date_str in trader's action to datetime object
    """
    date_time_obj = dt.strptime(date, '%Y/%m/%d %H:%M:%S')
    return date_time_obj


def helper_strdate_to_date_stock_action(date: str):
    """helper that change stock action's date to datetime object
    >>> date = '2010/10/20'
    >>> dt = helper_strdate_to_date_stock_action(date)
    >>> dt.strftime()

    """
    date_time_obj = dt.strptime(date, '%Y/%m/%d')
    return date_time_obj


def helper_strdate_to_date(date: str):
    """helper to change str date to datetime obj"""
    if ' ' in date:
        return helper_strdate_to_date_action(date)
    else:
        return helper_strdate_to_date_stock_action(date)


def bubble_sort(nums):
    """Use bubble sort to sort all_actions by their date of occurance"""
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            date1 = helper_strdate_to_date(nums[i].date)
            date2 = helper_strdate_to_date(nums[i+1].date)
            if date1 > date2:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


def show_output_of(list_action: list, stock_actions_list: list):
    """show the trading summury of a trader according to input actions"""
    t = Trader()
    actions_list = helper_load_stock_actions(stock_actions_list)
    actions_list.extend(helper_load_actions(list_action))
    bubble_sort(actions_list)
    t.set_all_actions(actions_list)
    for action in t.get_all_actions():
        t.update_account(action)
    t.update_action_by_date()
    return t.__repr__()
