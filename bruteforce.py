import time
from dataclasses import dataclass


@dataclass
class Stock:
    """Class to store data on a stock"""
    name: str
    value: int
    two_years_rate: float

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)


@dataclass
class StockPortfolio:
    """Class to stock a list of Stockes"""
    portfolio: list

    def get_global_income(self):
        return sum(stock.value * stock.two_years_rate
                   for stock in self.portfolio)

    def get_global_invest(self):
        return sum(stock.value for stock in self.portfolio)

    def __repr__(self):
        return f"Le portefeuille recommandé rapportera " \
               f"{self.get_global_income():.2f} euros au bout de 2 ans, " \
               f"pour {self.get_global_invest()} euros investis. \n" \
               f"Soit un taux global de " \
               f"{self.get_global_income()*100/500:.2f}%.\n"\
               f"Il nécessite : {self.portfolio}"


MAX_MONEY = 500
stocks = (
    Stock("Action-1", 20, 0.05),
    Stock("Action-2", 30, 0.10),
    Stock("Action-3", 50, 0.15),
    Stock("Action-4", 70, 0.20),
    Stock("Action-5", 60, 0.17),
    Stock("Action-6", 80, 0.25),
    Stock("Action-7", 22, 0.07),
    Stock("Action-8", 26, 0.11),
    Stock("Action-9", 48, 0.13),
    Stock("Action-10", 34, 0.27),
    Stock("Action-11", 42, 0.17),
    Stock("Action-12", 110, 0.09),
    Stock("Action-13", 38, 0.23),
    Stock("Action-14", 14, 0.01),
    Stock("Action-15", 18, 0.03),
    Stock("Action-16", 8, 0.08),
    Stock("Action-17", 4, 0.12),
    Stock("Action-18", 10, 0.14),
    Stock("Action-19", 24, 0.21),
    Stock("Action-20", 114, 0.18)
)


def timeit(func):
    """decorator to calculate the time taken by a function execution"""
    def timed(*args, **kw):
        start = time.perf_counter()
        result = func(*args, **kw)
        end = time.perf_counter()

        print(f"{func.__name__} a pris : "
              f"{(end-start)*1000:.2f} millisecondes.")
        return result
    return timed


def take_as_much_as_you_can(sorted_stocks: list, money: int) -> list:
    """function to take one of each stock in list
    until there is not enough money"""
    stock_list = []
    for stock in sorted_stocks:
        if money > stock.value:
            money -= stock.value
            stock_list.append(stock)

    return stock_list


@timeit
def simplest_solution(available_stocks: list) -> StockPortfolio:
    """simplest solution : take all best rated stock until there is no money
    function only used to have a approximation of result"""
    sorted_list = sorted(available_stocks,
                         key=lambda x: x.two_years_rate,
                         reverse=True)

    stock_list = take_as_much_as_you_can(sorted_list, MAX_MONEY)

    return StockPortfolio(stock_list)


@timeit
def bruteforce(available_stocks: tuple,
               max_money: int) -> StockPortfolio:
    """this function try all possible combinaisons of stocks
    with the max_money received in parameters"""
    """first sort all stocks 
    (so once we find a stock to expensive,
    we don't have to test the next in the list)"""
    sorted_list = sorted(available_stocks,
                         key=lambda x: x.value,
                         reverse=True)
    all_portfolios = []
    build_portfolio(sorted_list, max_money, [], all_portfolios)

    print(f"J'ai identifié {len(all_portfolios)} combinaisons possibles.")
    return max(all_portfolios, key=lambda x: x.get_global_income())


def build_portfolio(sorted_list: list, remaining_money: int,
                    building_list: list, all_portfolios: list):
    """Recursive fonction to iterate on each stock and each next
    in order to find all combinations as long as remaining money is > 0
    :param sorted_list list ordered of stock to iterate on
    :param remaining_money money still available to buy new stock
    :param building_list all stocks already taken in that iteration
    :param all_portfolios a list to store all combinaison found"""
    for index, stock in enumerate(sorted_list):
        if remaining_money >= stock.value:
            new_building_list = list(building_list)
            new_building_list.append(stock)
            build_portfolio(sorted_list[index+1:],
                            remaining_money-stock.value,
                            new_building_list,
                            all_portfolios)
        else:
            all_portfolios.append(StockPortfolio(building_list))


def fin():
    # print("La solution avec les actions les plus rentables est : ")
    # print(simplest_solution(stocks))
    # print()
    print("Pour nous la meilleure solution est :")
    print(bruteforce(stocks, MAX_MONEY))
    exit(0)


fin()
