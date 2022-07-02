from dataclasses import dataclass


@dataclass
class Stock:
    name: str
    value: int
    two_years_rate: float

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)


@dataclass
class StockPortfolio:
    portfolio: list
    """def __init__(self, stock_list: list, available_money: int):
        self.available_money = available_money
        self.stock_list = []
        for stock in stock_list:
            self.add_stock(stock)

    def add_stock(self, stock: Stock):
        if self.available_money >= stock.value:
            self.stock_list.append(stock)
            self.available_money -= stock.value
            return True
        else:
            return False"""

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
               f"{self.get_global_income()*100/500:.2f}.\n"\
               f"Il nécessite : {self.portfolio}"


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
