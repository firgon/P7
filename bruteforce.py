import time
from dataclasses import dataclass
import numpy as np


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
stocks = (
    Stock("Action-1", 20, 0.05*20),
    Stock("Action-2", 30, 0.10*30),
    Stock("Action-3", 50, 0.15*50),
    Stock("Action-4", 70, 0.20*70),
    Stock("Action-5", 60, 0.17*60),
    Stock("Action-6", 80, 0.25*80),
    Stock("Action-7", 22, 0.07*22),
    Stock("Action-8", 26, 0.11*26),
    Stock("Action-9", 48, 0.13*48),
    Stock("Action-10", 34, 0.27*34),
    Stock("Action-11", 42, 0.17*42),
    Stock("Action-12", 110, 0.09*110),
    Stock("Action-13", 38, 0.23*38),
    Stock("Action-14", 14, 0.01*14),
    Stock("Action-15", 18, 0.03*18),
    Stock("Action-16", 8, 0.08*8),
    Stock("Action-17", 4, 0.12*4),
    Stock("Action-18", 10, 0.14*10),
    Stock("Action-19", 24, 0.21*24),
    Stock("Action-20", 114, 0.18*114)
)


def timeit(func):
    """decorator to calculate the time taken by a function execution"""
    def timed(*args, **kw):
        start = time.perf_counter()
        result = func(*args, **kw)
        end = time.perf_counter()

        print(f"*** {func.__name__} a pris : "
              f"{(end-start):.4f} secondes. ***")
        return result
    return timed


def calculate_income(stocks_list) -> float:
    return sum(stock.income for stock in stocks_list)


@timeit
def bruteforce(available_stocks: tuple,
               max_money: int) -> StockPortfolio:
    """this function try all possible combinaisons of stocks
    with the max_money received in parameters by using dynamic algorithm"""
    table = np.zeros((len(available_stocks)+1, max_money*100+1),
                     dtype=np.float32)
    keep = np.zeros((len(available_stocks)+1, max_money*100+1),
                    dtype=np.int32)

    for i in np.arange(1, len(available_stocks)+1):
        for j in np.arange(max_money*100+1):
            value = round(available_stocks[i-1].value * 100)
            income = available_stocks[i-1].income
            if (value <= j) \
                    and (income + table[i-1, j - value] > table[i-1, j]):
                table[i, j] = income + table[i-1, j - value]
                keep[i, j] = 1
            else:
                table[i, j] = table[i-1, j]

    remaining_money = max_money*100
    building_portfolio = []

    for i in np.arange(len(available_stocks), 0, -1):
        if keep[i, remaining_money] == 1:
            stock = available_stocks[i-1]
            building_portfolio.append(stock)
            remaining_money -= int(stock.value*100)

    return StockPortfolio(building_portfolio,
                          calculate_income(building_portfolio))


print()
print(f"Recherche sur {len(stocks)} actions :")
print()
print("La solution de force brute vous propose :")
print(bruteforce(stocks, MAX_MONEY))
