import time
from dataclasses import dataclass
from tkinter import filedialog
import csv


@dataclass
class Stock:
    """Class to store data on a stock"""
    name: str
    value: float
    income: float

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def rate(self):
        return self.income/self.value


@dataclass
class StockPortfolio:
    """Class to stock a list of Stockes"""
    portfolio: list
    income: float

    def get_global_invest(self):
        return sum(stock.value for stock in self.portfolio)

    def __repr__(self):
        return f"Le portefeuille recommandé rapportera " \
               f"{self.income:.2f} euros au bout de 2 ans, " \
               f"pour {self.get_global_invest():.2f} euros investis. \n" \
               f"Soit un taux global de " \
               f"{self.income*100/500:.2f}%.\n"\
               f"Il nécessite : {self.portfolio}"


MAX_MONEY = 500


def timeit(func):
    """decorator to calculate the time taken by a function execution"""
    def timed(*args, **kw):
        start = time.perf_counter()
        result = func(*args, **kw)
        end = time.perf_counter()

        print(f"{func.__name__} a pris : "
              f"{(end-start):.4f} secondes.")
        return result
    return timed


def take_as_much_as_you_can(sorted_stocks: list, money: int) -> list:
    """function to take one of each stock in list
    as long as there is enough money"""
    stock_list = []
    for stock in sorted_stocks:
        if money > stock.value:
            money -= stock.value
            stock_list.append(stock)

    return stock_list


@timeit
def simplest_solution(available_stocks: list, max_money: int) \
        -> StockPortfolio:
    """simplest solution : take all best rated stock until there is no money
    function only used to have a approximation of result"""

    sorted_list = sorted(available_stocks,
                         key=lambda x: x.rate(),
                         reverse=True)

    stock_list = take_as_much_as_you_can(sorted_list, max_money)

    return StockPortfolio(stock_list, calculate_income(stock_list))


def calculate_income(stocks_list) -> float:
    return sum(stock.income for stock in stocks_list)


def read_values_csv() -> list:
    result = []

    choice = filedialog.askopenfilename()

    with open(choice, "r") as file:
        reader = csv.DictReader(file)

        for line in reader:
            price = float(line['price'])
            if price <= 0:
                continue
            result.append(Stock(line['name'],
                                price,
                                price * float(line['profit'])/100))

    return result


stocks = read_values_csv()

print()
print(f"Recherche sur {len(stocks)} actions :")
print()
print("La solution optimisée vous propose :")
print(simplest_solution(stocks, MAX_MONEY))
