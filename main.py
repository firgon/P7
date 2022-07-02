from data import stocks, StockPortfolio
import time

MAX_MONEY = 500


def timeit(func):
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


# simplest solution : take all best rated stock until there is no money
@timeit
def simplest_solution(available_stocks: list) -> StockPortfolio:
    sorted_list = sorted(available_stocks,
                         key=lambda x: x.two_years_rate,
                         reverse=True)

    stock_list = take_as_much_as_you_can(sorted_list, MAX_MONEY)

    return StockPortfolio(stock_list)


@timeit
def bruteforce(available_stocks: tuple) -> StockPortfolio:
    sorted_list = sorted(available_stocks,
                         key=lambda x: x.value,
                         reverse=True)
    all_portfolios = []
    build_portfolio(sorted_list, MAX_MONEY, [], all_portfolios)

    return max(all_portfolios, key=lambda x: x.get_global_income())


def build_portfolio(sorted_list: list, remaining_money: int,
                    building_list: list, all_portfolios: list):
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
    print("La solution avec les actions les plus rentables est : ")
    print(simplest_solution(stocks))
    print()
    print("Mais la meilleure solution est :")
    print(bruteforce(stocks))
    exit(0)


fin()
